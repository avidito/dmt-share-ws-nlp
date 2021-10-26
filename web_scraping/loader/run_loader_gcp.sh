#!/bin/bash

##############################################################
# Program: Load scraping result to Postgres database.
# Parameter: -
# Example:
#   bash run_loader.sh
##############################################################

##### Variables #####
project_dir=$SCRAPER_PROJECT_DIR
result_dir=$SCRAPER_RESULT_DIR
dml_dir="$SCRAPER_PROJECT_DIR/loader/dml"
gcp_bucket="gs://dmt_share_leorio"

##### Main #####
# Copy file to GCS and backup in local VM
echo "[$(date '+%Y-%m-%d %H:%M:%S')] INFO - Copy file to GCS and backup in local VM"
cp "$result_dir/scraping_result.csv" "$backup_dir/scraping_result-$job_date.csv"
gsutil -m cp "$result_dir/scraping_result.csv" "gs://$gcp_bucket/src/scraping_result/"
gsutil -m cp "$result_dir/scraping_result.csv" "gs://$gcp_bucket/bkp/scraping_result/scraping_result-$job_date.csv"

# Loading data and remove duplicate
echo "[$(date '+%Y-%m-%d %H:%M:%S')] INFO - Loading data and remove duplicate"
bq query --use_legacy_sql=false --quiet=true "$(cat "$dml_dir/transform_cdc_remove_duplicate_tmp.sql")" >> /dev/null 2>&1
bq query --use_legacy_sql=false --quiet=true "$(cat "$dml_dir/load_from_tmp_to_src.sql")" >> /dev/null 2>&1

# Remove data from result directory in local VM and GCS
echo "[$(date '+%Y-%m-%d %H:%M:%S')] INFO - Remove data from result directory in local VM and GCS"
rm "$result_dir/scraping_result.csv"
gsutil -m rm "gs://$gcp_bucket/src/scraping_result/"

#!/bin/bash

##############################################################
# Program: Load scraping result to Postgres database.
# Parameter: -
# Example:
#   bash run_loader.sh
##############################################################

##### Variables #####
hostname='database'
user='admin'
password='admin'
database='dmt_share'
result_dir='/app/web_scraping/result/scraping_result.csv'
dml_dir='/app/web_scraping/loader/dml'
upload_query=$(cat "$dml_dir/load_from_csv_to_cdc.sql")

##### Main #####
PGPASSWORD=$password psql -h $hostname -U $user -d $database -c "$upload_query" -q
PGPASSWORD=$password psql -h $hostname -U $user -d $database -f "$dml_dir/transform_cdc_remove_duplicate.sql" -q
PGPASSWORD=$password psql -h $hostname -U $user -d $database -f "$dml_dir/load_from_cdc_to_src.sql" -q

#!/usr/bin/bash

##############################################################
# Program: Running web-scraping Python script spesific date.
# Parameter:
#   - job_date: %Y-%m-%d format (DEFAULT: yesterday)
# Example:
#   sh run_scraper.sh 2021-09-22
##############################################################

##### Variables #####
project_dir=$SCRAPER_PROJECT_DIR
result_dir=$SCRAPER_RESULT_DIR
backup_dir=$SCRAPER_BACKUP_DIR
job_date=$1

if [[ $job_date = '' ]]; then
  echo "job_date wasn't provided. Use default value."
  job_date=`date -d "1 days ago" '+%Y-%m-%d'`
fi

##### Main #####
echo "[$(date '+%Y-%m-%d %H:%M:%S')] INFO - Running Scraper with date: $job_date"
python3 "$project_dir/scraper/run_scraper.py" $job_date

echo "[$(date '+%Y-%m-%d %H:%M:%S')] INFO - Loading Scraper result to database"
if test -f "$result_dir/scraping_result.csv"; then
  cp "$result_dir/scraping_result.csv" "$backup_dir/scraping_result-$job_date.csv"
  #bash "$project_dir/loader/run_loader.sh"
  rm "$result_dir/scraping_result.csv"
else
  echo "$result_dir/scraping_result.csv is not exists"
fi

echo "[$(date '+%Y-%m-%d %H:%M:%S')] INFO - Scraper job is finish"
exit 0

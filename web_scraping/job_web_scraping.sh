#!/usr/bin/bash

##############################################################
# Program: Running web-scraping Python script spesific date.
# Parameter:
#   - job_date: %Y-%m-%d format (DEFAULT: yesterday)
# Example:
#   sh run_scraper.sh 2021-09-22
##############################################################

##### Variables #####
job_date=$1

if [[ $job_date = '' ]]; then
  echo "job_date wasn't provided. Use default value."
  job_date=`date -d "1 days ago" '+%Y-%m-%d'`
fi

##### Main #####
echo "Running Scraper with date: $job_date"
python $PROJECT_DIR/scraper/run_scraper.py $job_date

echo "Backup result"
cp $RESULT_DIR/scraping_result.csv "$BACKUP_DIR/scraping_result-$job_date.csv"

echo "Loading Scraper result to database"
bash $PROJECT_DIR/loader/run_loader.sh
rm $RESULT_DIR/scraping_result.csv

exit 0

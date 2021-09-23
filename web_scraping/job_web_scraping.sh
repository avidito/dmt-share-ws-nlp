#!/usr/bin/bash

##############################################################
# Program: Running web-scraping Python script spesific date.
# Parameter:
#   - job_date: %Y-%m-%d format (DEFAULT: yesterday)
# Example:
#   sh run_scraper.sh 2021-09-22
##############################################################

source ~/.bash_profile

##### Variables #####
vjob_date=$1

if [[ $vjob_date = '' ]];
then
  echo "vjob_date wasn't provided. Use default value."
  vjob_date=`date -d "1 days ago" '+%Y-%m-%d'`
fi

##### Main #####
echo "Running Scraper with date: $vjob_date"
python /app/scraper/run.py $vjob_date

echo "Loading Scraper result to database"


exit 0

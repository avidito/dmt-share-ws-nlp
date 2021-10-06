##############################################################
# Program: Running web-scraping Python script spesific date.
# Parameter:
#   - job_date: %Y-%m-%d format (DEFAULT: yesterday)
# Example:
#   & .\run_scraper.ps1 2021-09-22
##############################################################

##### Variables #####
$PROJECT_DIR=$env:SCRAPER_PROJECT_DIR
$RESULT_DIR=$env:SCRAPER_RESULT_DIR
$BACKUP_DIR=$env:SCRAPER_BACKUP_DIR
$job_date=$args[0]

if ( $job_date -eq $null) {
  Write-Host "job_date wasn't provided. Use default value."
  $job_date=(Get-Date -UFormat "%Y-%m-%d")
}

##### Main #####
Write-Host "Running Scraper with date: $job_date"
python $PROJECT_DIR/scraper/run_scraper.py $job_date

Write-Host "Backup result"
Copy-Item $RESULT_DIR/scraping_result.csv -Destination "$BACKUP_DIR/scraping_result-$job_date.csv"

Write-Host "Loading Scraper result to database"
& $PROJECT_DIR/loader/run_loader.ps1
Remove-Item $RESULT_DIR/scraping_result.csv

exit 0

##############################################################
# Program: Running web-scraping Python script spesific date.
# Parameter:
#   - job_date: %Y-%m-%d format (DEFAULT: yesterday)
# Example:
#   & .\run_scraper.ps1 2021-09-22
##############################################################

##### Variables #####
$project_dir = $env:SCRAPER_PROJECT_DIR
$result_dir = $env:SCRAPER_RESULT_DIR
$backup_dir = $env:SCRAPER_BACKUP_DIR
$job_date = $args[0]

if ($job_date -eq $null) {
  Write-Host "job_date wasn't provided. Use default value."
  $job_date=(Get-Date).AddDays(-1).ToString("yyyy-MM-dd")
}

##### Main #####
Write-Host "Running Scraper with date: $job_date"
python "$PROJECT_DIR\scraper\run_scraper.py" $job_date

Write-Host "Loading Scraper result to database"
if (Test-Path -Path "$result_dir\scraping_result.csv") {
  Copy-Item "$result_dir\scraping_result.csv" -Destination "$backup_dir/scraping_result-$job_date.csv"
  & "$project_dir\loader\run_loader.ps1"
  Remove-Item "$result_dir\scraping_result.csv"
} else {
  Write-Host "$result_dir\scraping_result.csv is not exists"
}

exit 0

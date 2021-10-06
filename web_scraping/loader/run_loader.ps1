##############################################################
# Program: Load scraping result to Postgres database.
# Parameter: -
# Example:
#   bash run_loader.sh
##############################################################

##### Variables #####
$project_dir = $env:SCRAPER_PROJECT_DIR
$result_dir = $env:SCRAPER_RESULT_DIR
$hostname = $env:SCRAPER_DATABASE_HOST

$user = "admin"
$password = "admin"
$database = "dmt_share"
$dml_dir = "$project_dir\loader\dml"
$upload_query = (Get-Content "$dml_dir\load_from_csv_to_cdc.sql") -replace "{{result_dir}}","$result_dir\"

##### Main #####
$env:PGPASSWORD = "$password"; psql -h $hostname -U $user -d $database -c "$upload_query" -q
$env:PGPASSWORD = "$password"; psql -h $hostname -U $user -d $database -f "$dml_dir\transform_cdc_remove_duplicate.sql" -q
$env:PGPASSWORD = "$password"; psql -h $hostname -U $user -d $database -f "$dml_dir\load_from_cdc_to_src.sql" -q

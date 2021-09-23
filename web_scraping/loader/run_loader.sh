##############################################################
# Program: Load scraping result to Postgres database.
# Parameter:
#   - hostname: database host (DEFAULT: database)
#   - user: database admin username (DEFAULT: admin)
#   - password: database admin password (DEFAULT: admin)
#   - database: name of database (DEFAUL: dmt_share)
# Example:
#   sh run_loader.sh
##############################################################

source ~/.bash_profile

##### Variables #####
hostname=$1
user=$3
password=$4

if [[ $hostname = '' ]];
then
  hostname='database'
fi
if [[ $user = '' ]];
then
  user='admin'
fi
if [[ $password = '' ]];
then
  password='admin'
fi
if [[ $database = '' ]];
then
  $database='dmt_share'
fi

$dml_dir='/app/web_scraping/loader'

##### Main #####
PGPASSWORD=$password

psql -h $host -U $user -d $database -f $dml_dir/load_from_csv_to_cdc.sql
psql -h $host -U $user -d $database -f $dml_dir/transform_cdc_remove_duplicate.sql
psql -h $host -U $user -d $database -f $dml_dir/load_from_cdc_to_src.sql

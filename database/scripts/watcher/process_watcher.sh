#!/bin/bash

process_dir="/data/prc"

# Start Watcher for file creation and migration
inotifywait -m -e create -e moved_to $landing_dir |
while read dir op file
do
  echo "Spotted: '$file'"

  # If file is in .csv format, start data insertion
  if [[ "$file" = *.csv ]]; then
    echo "Starting loading from csv to cdc"
    psql -f load_from_cdc_to_src.sql 
  fi
done

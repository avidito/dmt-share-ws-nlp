#!/bin/bash

landing_dir="/landing"
backup_dir="/data/bkp"
process_dir="/data/prc"

inotifywait -m -e create -e moved_to $landing_dir |
while read dir op file
do
	if [[ "$file" = *.csv ]]; then
		# Copy CSV file to backup
		echo "Spot $file"
		echo "Copy to $backup_dir"
		cp $landing_dir/$file $backup_dir/

		# Move CSV file to process
		result_file="$(echo $file | cut -d'-' -f 1 | cut -d'.' -f 1).csv"
		echo "Move to $process_dir as $result_file"
		mv $landing_dir/$file $process_dir/$result_file
	fi
done

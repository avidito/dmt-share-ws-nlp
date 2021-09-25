import os
import csv
from datetime import datetime

def aggregate_result(result_dir, filename, add_date=False, drop_data=True):
    """
    Aggregate result data into single file.
    """

    # Get list of tmp results
    agg_filename = filename + "_" + datetime.now().strftime("%Y%m%d") if (add_date) else filename
    agg_filename = f"{agg_filename}.csv"
    list_of_filepath = [
        os.path.join(result_dir, src_filename)
        for src_filename in os.listdir(result_dir) if (src_filename != agg_filename)
    ]

    # Open write connection to aggregate file
    agg_filepath = os.path.join(result_dir, agg_filename)
    with open(agg_filepath, "w+", encoding="utf-8", newline="") as agg_file:
        agg_writer = csv.writer(agg_file)

        # Read each tmp result and write it to aggregate file
        for i, filepath in enumerate(list_of_filepath):
            with open(filepath, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                rows = [row for row in reader]

            # Write data to agg_file
            if (i):
                agg_writer.writerows(rows[1:])
            else:
                agg_writer.writerows(rows) # Include header for the first file

    # Delete tmp results
    if (drop_data == True):
        for filepath in list_of_filepath:
            os.remove(filepath)

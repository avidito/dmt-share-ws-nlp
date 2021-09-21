import os
import csv

def aggregate_result(result_dir, level, file_prefix, drop_data=True):
    """
    Aggregate result data into single file by level
    """

    # Agregration level: All category and all website
    if (level == "all"):
        # Get list of tmp results
        agg_filename = f"{file_prefix}-all.csv"
        list_of_result_filepath = [
            os.path.join(result_dir, filename)
            for filename in os.listdir(result_dir) if (filename != agg_filename)
        ]

        # Open write connection to aggregate file
        agg_filepath = os.path.join(result_dir, agg_filename)
        with open(agg_filepath, "w+", encoding="utf-8", newline="") as agg_file:
            agg_writer = csv.writer(agg_file)

            # Read each tmp result and write it to aggregate file
            for i, result_filepath in enumerate(list_of_result_filepath):
                with open(result_filepath, "r", encoding="utf-8") as result_file:
                    result_reader = csv.reader(result_file)
                    rows = [row for row in result_reader]

                if (i):
                    agg_writer.writerows(rows[1:])
                else:
                    agg_writer.writerows(rows) # Include header for the first file

        # Delete tmp results
        if (drop_data == True):
            for filepath in list_of_result_filepath:
                os.remove(filepath)

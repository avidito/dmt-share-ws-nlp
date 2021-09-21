#################### Scraper ####################
# How to Run:
#   python run.py [DATE] [RESULT_PREFIX]
#
# *DEFAULT value for DATE is current date.
# *DEFAULT value for RESULT_PREFIX is 'scraping_result'.
#
# Example:
#   python run.py 2021-09-07
#################################################
import os
from datetime import datetime

from scraper import run_scraper

from shared.module.params import get_args, get_config_json
from shared.module.aggregator import aggregate_result

if __name__ == "__main__":
    # Get configuration values
    config = get_config_json("config.json")
    driver = config["driver"]
    output_dir = config["output_dir"]
    scraper_config = config["scraper"]

    # Get arguments values
    [date_str, filename] = get_args(params_count = 2)
    date = datetime.strptime(date_str, "%Y-%m-%d") if (date_str) else datetime.now()
    filename = filename if (filename) else "scraping_result"

    # Create output_dir if not exists
    if (not os.path.exists(output_dir)):
        os.makedirs(output_dir)

    # Run kompas scraper
    run_scraper(
        scraper_id = "kompas",
        config = scraper_config["kompas"],
        date = date,
        output_dir = output_dir
    )

    # Run cnn scraper
    run_scraper(
        scraper_id = "cnn",
        config = scraper_config["cnn"],
        date = date,
        output_dir = output_dir,
        driver = driver
    )

    # Aggregate result
    print(f"Aggreating result into single file: {filename}.csv")
    aggregate_result(output_dir, filename, add_date = True)

#################### Scraper ####################
# How to Run:
#   python run.py [DATE]
#
# *DEFAULT value for DATE is current date.
#
# Example:
#   python run.py 2021-09-07
#################################################
import os

from scraper import run_scraper
from shared.module.params import get_args, get_config_json
from shared.module.aggregator import aggregate_result

if __name__ == "__main__":
    # Get configuration values
    config = get_config_json("config.json")
    driver = config["driver"]
    output_dir = config["output_dir"]
    aggregation_level = config["aggregation_level"]
    scraper_config = config["scraper"]

    # Get arguments values
    [date_str] = get_args(params_count = 1)

    # Create output_dir if not exists
    if (not os.path.exists(output_dir)):
        os.makedirs(output_dir)

    # Run kompas scraper
    # run_scraper(
    #     scraper_id = "kompas",
    #     config = scraper_config["kompas"],
    #     date_str = date_str,
    #     output_dir = output_dir
    # )

    # Run cnn scraper
    run_scraper(
        scraper_id = "cnn",
        config = scraper_config["cnn"],
        date_str = date_str,
        output_dir = output_dir,
        driver = driver
    )

    # Aggregate result
    aggregate_result(output_dir, aggregation_level)

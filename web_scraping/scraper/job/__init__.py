import os

from .kompas import KompasScraper
from .cnn import CNNScraper
from shared.module.params import get_date_params

Scraper = {
    "kompas": KompasScraper,
    "cnn": CNNScraper
}

def run_scraper(scraper_id, config, date, output_dir, **kwargs):
    """
    Running scraper
    """

    print(f"Start running: {scraper_id} scraper")
    channels = config["channels"]
    for channel in channels:
        scraper = Scraper[scraper_id](
            channel = channel["name"],
            category = channel["category"],
            start_url = channel["url"],
            start_url_params = get_date_params(date, config["time_format"], channel["type"]),
            output_dir = output_dir,
            **kwargs
        )

        scraper.run(
            filename = f"{scraper_id}_{channel['name']}_{date.strftime('%Y%m%d')}.csv",
            multipage = config["multipage"]
        )
    print(f"Finish running: {scraper_id} scraper")

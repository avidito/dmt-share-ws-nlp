from datetime import datetime
import os

from .kompas import KompasScraper
from .cnn import CNNScraper
from shared.module.params import get_date_params

Scraper = {
    "kompas": KompasScraper,
    "cnn": CNNScraper
}

def run_scraper(scraper_id, config, date_str, output_dir, **kwargs):
    """
    Running scraper
    """

    date = datetime.strptime(date_str, "%Y-%m-%d") if (date_str) else datetime.now()
    channels = config["channels"]

    print(f"Start running: {scraper_id} scraper")
    for channel in channels:
        scraper = Scraper[scraper_id](
            channel = channel["name"],
            general_category = channel["general_category"],
            start_url = channel["url"],
            start_url_params = get_date_params(date, config["time_format"], channel["type"]),
            output_dir = output_dir,
            **kwargs
        )

        scraper.run(
            filename = f"kompas_{channel['name']}_{date.strftime('%Y%m%d')}.csv",
            multipage = config["multipage"]
        )
    print(f"Finish running: {scraper_id} scraper")

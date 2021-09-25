import requests
import time
from bs4 import BeautifulSoup
import csv
import os

class Scraper:
    def __init__(self, start_url=None, start_url_params=None, website="", delay=10, output_dir=""):
        self.start_url = start_url
        self.start_url_params = start_url_params
        self.website = website
        self.delay = delay
        self.output_dir = output_dir

        self.info = []
        self.info_cnt = 0
        self.page_cnt = 0

    def run(self, start_url=None, export=True, filename="result.csv", multipage=False):
        """
        Starting web scraping process
        """

        # Check minimum parameters to start scraping
        if (start_url is None) and (self.start_url is None):
            raise ValueError("'start_url' must be defined!")
        start_url = start_url if (start_url) else self.start_url

        # Start extracting information
        [current_url, page] = self.navigate_page(start_url, **self.start_url_params)

        # Extract multipage (pagination)
        if (multipage):
            while(1):
                info = self.extract_info(current_url, page)
                self.save_info(info)
                next_url = self.get_next_page(page)
                if (next_url):
                    [current_url, page] = self.navigate_page(next_url)
                else:
                    break
        # Extract single page
        else:
            info = self.extract_info(current_url, page)
            self.save_info(info)

        # Export data
        if (export):
            self.export_data(filename)

    ##### Scraping Method #####
    def navigate_page(self, url, path=None, query=None):
        """
        Default page navigation method
        """

        url = requests.compat.urljoin(url, path) if (path) else url
        req = requests.get(url, params=query)

        status = "OK" if (req.status_code == 200) else f"NOT OK: ERROR {req.status_code}"
        print(f"Requesting Page: {url} | Status Code: {status}")
        time.sleep(self.delay)

        return req.url, BeautifulSoup(req.content, features="lxml")

    def extract_info(self, current_url, page):
        """
        Default information extraction from page
        """

        return {"msg": "`extract_info` is not implemented. Try to override this method."}

    def get_next_page(self, page):
        """
        Default method to get next page (only for multipage run)
        """

        return None

    def save_info(self, info):
        """
        Default method to saving information
        """

        if (isinstance(info, list)):
            self.info.extend(info)
        else:
            self.info.append(info)

    def export_data(self, filename="result.csv"):
        """
        Default data export
        """
        filepath = os.path.join(self.output_dir, filename)

        if (len(self.info)):
            header = self.info[0].keys()
            rows = [list(i.values()) for i in self.info]
            with open(filepath, "w+", encoding="utf-8", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(rows)

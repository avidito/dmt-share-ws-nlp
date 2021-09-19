import time

from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException

from shared.module.scraper import Scraper
from shared.module.selenium import get_driver

class CNNScraper(Scraper):
    def __init__(self, channel, general_category, driver, **kwargs):
        super().__init__(**kwargs)
        self.website = "kompas"
        self.channel = channel
        self.general_category = general_category
        self.driver = driver

    def extract_info(self, current_url, page):
        # Get page generate all news
        driver = get_driver(self.driver)
        driver.get(current_url)

        while(1):
            try:
                load_more = driver.find_element_by_class_name("loading")
                load_more.click()
                print("Add more result by clicking 'Selanjutnya' button")
                time.sleep(5)
            except NoSuchElementException as e:
                break

        new_page = BeautifulSoup(driver.page_source, "lxml")
        driver.quit()

        # Extract all news info
        article_list = new_page.find("div", class_="media_rows").find_all("article")

        list_of_info = []
        for article in article_list:
            info = {
                "website": self.website,
                "channel": self.channel,
                "general_category": self.general_category,
                "title": article.find("h2", class_="title").text,
                "url": article.find("a").get("href"),
                "category": article.find("span", class_="kanal").text,
            }
            list_of_info.append(info)

        return list_of_info

import time

from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

from shared.scraper import SeleniumScraper
from shared.selenium import get_driver

class CNNScraper(SeleniumScraper):
    def __init__(self, date_str, channel, category, **kwargs):
        super().__init__(**kwargs)
        self.website = "cnn"
        self.date_str = date_str
        self.channel = channel
        self.category = category

    def extract_info(self):
        # Get page generate all news
        while(1):
            try:
                load_more = self.driver.find_element_by_class_name("btn__more")
                load_more.click()
                print("Add more result by clicking 'Selanjutnya' button")
                time.sleep(5)
            except NoSuchElementException as e:
                break
            except ElementClickInterceptedException as e:
                break

        new_page = BeautifulSoup(self.driver.page_source, features="html.parser")

        # Extract all news info
        list_of_info = []
        article_section = new_page.find("div", class_="media_rows")
        if (article_section):
            article_list = article_section.find_all("article")

            for article in article_list:
                info = {
                    "title": article.find("h2", class_="title").text,
                    "website": self.website,
                    "channel": self.channel,
                    "category": self.category,
                    "native_category": article.find("span", class_="kanal").text,
                    "url": article.find("a").get("href"),
                    "publish_dt": self.date_str
                }
                list_of_info.append(info)

        return list_of_info

from utils.scraper import Scraper

class KompasScraper(Scraper):
    def __init__(self, channel, category, **kwargs):
        super().__init__(**kwargs)
        self.website = "kompas"
        self.channel = channel
        self.category = category

    def extract_info(self, current_url, page):
        article_list = page.find_all("div", class_="article__list")

        list_of_info = []
        for article in article_list:
            info = {
                "title": article.find("a", class_="article__link").text,
                "website": self.website,
                "channel": self.channel,
                "category": self.category,
                "native_category": article.find("div", class_="article__subtitle").text,
                "url": article.find("a", class_="article__link").get("href")
            }
            list_of_info.append(info)

        return list_of_info

    def get_next_page(self, page):
        next_button = page.find("a", attrs={"class": "paging__link"}, string="Next")
        next_url = next_button["href"] if (next_button) else None
        return next_url

import scrapy
import requests
from scrapy import Item

category_url_class = "a.pr-1edcde9"
entry_url = "https://www.pricerunner.com"


def menu_item_list():
    response = requests.get("https://www.pricerunner.com/public/navigation/menu/uk/items")
    result = []
    top_menu_item = response.json()["topMenuItems"]
    for menu_item in top_menu_item:
        result.append(entry_url + menu_item["path"])
    return result


class CategorySpider(scrapy.Spider):
    name = "category"
    start_urls = menu_item_list()

    def parse(self, response):
        urls = UrlData()
        urls["urls"] = []
        sub_categories = response.css(category_url_class)
        for sub_category in sub_categories:
            if "?attr_" not in sub_category.attrib["href"]:
                break
            urls["urls"].append(entry_url + sub_category.attrib["href"])
        yield urls


class UrlData(Item):
    urls = scrapy.Field()

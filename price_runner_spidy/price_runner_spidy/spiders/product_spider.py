import requests
import scrapy
from twisted.internet import reactor, defer
from twisted.trial import runner
from scrapy.item import Item, Field
from price_runner_spidy.price_runner_spidy.spiders.category_spider import CategorySpider

product_component_name = 'div.pr-1k8dg1g'
sub_category_component_class_name = "div.i54RWUrpDG"
entry_url = "https://www.pricerunner.com"


class PriceRunnerSpider(scrapy.Spider):
    name = "products"
    start_urls = []
    custom_settings = {"ITEM_PIPELINES": {
        'price_runner_spidy.price_runner_spidy.pipelines.PriceRunnerSpidyPipeline': 300,
    }}

    def parse(self, response):
        product_components = response.css(product_component_name)
        for product_component in product_components:
            product_item = ProductItem()
            if not product_component.css("a"):
                break
            product_dict = dict()
            product_item["category"] = response.css("a.EWsqM2HIwb").css("span::text").extract()[-1]
            product_item["sub_category"] = response.css("h1.pr-lilhn6::text").extract()[0]
            product_item["name"] = product_component.css("h3::text").extract()[0]
            try:
                product_item["description"] = product_component.css("p.pr-13b83wt::text").extract()[0]
            except IndexError:
                product_item["description"] = ""
            product_item["id"] = entry_url + product_component.css("a").attrib["href"]
            product_item["url"] = entry_url + product_component.css("a").attrib["href"]
            product_item["price"] = product_component.css("span.pr-be5x0o::text").extract()[0]
            try:
                product_item["overall_rank"] = product_component.css("p.pr-1ob9nd8::text").extract()[0]
            except IndexError:
                product_item["overall_rank"] = 0
            product_item["sub_title"] = ""

            yield product_item


class ProductItem(Item):
    id = Field()
    category = Field()
    sub_category = Field()
    name = Field()
    description = Field()
    url = Field()
    price = Field()
    overall_rank = Field()
    sub_title = Field()

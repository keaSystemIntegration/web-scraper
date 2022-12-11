import requests
import scrapy

product_component_name = 'div.pr-1k8dg1g'
sub_category_component_class_name = "div.i54RWUrpDG"
entry_url = "https://www.pricerunner.com"


class PriceRunnerSpider(scrapy.Spider):
    name = "products"
    # start_urls = ["https://www.pricerunner.com/cl/165/Game-Controllers?attr_100003493=100014244"]

    def __int__(self, *args, **kwargs):
        super(PriceRunnerSpider, self).__init__(*args, **kwargs)
        self.start_urls = kwargs.get('start_urls').split(',')

    def parse(self, response):
        product_components = response.css(product_component_name)

        for product_component in product_components:
            if not product_component.css("a"):
                break
            product_dict = dict()
            product_dict["category"] = response.css("a.EWsqM2HIwb").css("span::text").extract()[-1]
            product_dict["sub_category"] = response.css("h1.pr-lilhn6::text").extract()[0]
            product_dict["name"] = product_component.css("h3::text").extract()[0]
            try:
                product_dict["description"] = product_component.css("p.pr-13b83wt::text").extract()[0]
            except IndexError:
                product_dict["description"] = ""
            product_dict["url"] = entry_url + product_component.css("a").attrib["href"]
            product_dict["price"] = product_component.css("span.pr-be5x0o::text").extract()[0]
            try:
                product_dict["overall_rank"] = product_component.css("p.pr-1ob9nd8::text").extract()[0]
            except IndexError:
                product_dict["overall_rank"] = 0
            product_dict["sub_title"] = ""
            print(product_dict)
            print("---------------------------------")
            # product_dir needs to insert product to sqlite file

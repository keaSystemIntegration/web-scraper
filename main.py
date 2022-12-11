from price_runner_spidy import price_runner_spidy
from scrapy.crawler import CrawlerProcess

from price_runner_spidy.price_runner_spidy.spiders.category_spider import CategorySpider

process = CrawlerProcess()
process.crawl(CategorySpider)
process.start()


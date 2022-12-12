from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

from price_runner_spidy.price_runner_spidy.spiders.category_spider import CategorySpider
from price_runner_spidy.price_runner_spidy.spiders.product_spider import PriceRunnerSpider

configure_logging()
settings = get_project_settings()
runner = CrawlerRunner(settings)

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(CategorySpider)
    yield runner.crawl(PriceRunnerSpider, start_urls=CategorySpider().result)
    #yield runner.crawl(PriceRunnerSpider, start_urls=["https://www.pricerunner.com/cl/94/Headphones?attr_100003567=100014541"])
    reactor.stop()


crawl()
reactor.run()

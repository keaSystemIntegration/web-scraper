from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

from price_runner_spidy.price_runner_spidy.spiders.category_spider import CategorySpider
from price_runner_spidy.price_runner_spidy.spiders.product_spider import PriceRunnerSpider

settings = get_project_settings()
configure_logging(settings)
runner = CrawlerRunner(settings)

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(CategorySpider)
    print("$$$$$$$$$$$")
    print(CategorySpider().result)
    print("$$$$$$$$$$$")
    yield runner.crawl(PriceRunnerSpider, start_urls=CategorySpider().result)
    reactor.stop()


crawl()
reactor.run()

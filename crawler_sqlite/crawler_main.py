from crawler_sqlite.send_sqlite import send_sqlite_over_sftp
from price_runner_spidy.price_runner_spidy.spiders.category_spider import CategorySpider
from price_runner_spidy.price_runner_spidy.spiders.product_spider import PriceRunnerSpider
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings


@defer.inlineCallbacks
def crawl():    
    configure_logging()
    settings = get_project_settings()
    runner = CrawlerRunner(settings)
    yield runner.crawl(CategorySpider)
    yield runner.crawl(PriceRunnerSpider, start_urls=CategorySpider().result)
    # yield runner.crawl(PriceRunnerSpider, start_urls=[
    # "https://www.pricerunner.com/cl/94/Headphones?attr_100003567=100014541"])
    reactor.stop()


def execute_crawler():
    crawl()
    reactor.run()
    print("=====================================")
    print("Crawler finished")
    print("=====================================")
    send_sqlite_over_sftp()


# 事実上,デバッグ用のツール

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


from connpass.spiders.api import ApiSpider


def search_my_event(nickname='shinyorke', count=100):
    settings = get_project_settings()
    crawler = CrawlerProcess(settings)
    crawler.crawl(ApiSpider, nickname=nickname, count=count)
    crawler.start()


if __name__ == '__main__':
    search_my_event()
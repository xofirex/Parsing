import os

import scrapy
import pandas as pd
from train.items import Book


class BookSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/catalogue/page-1.html"]
    BASE_URL = 'http://books.toscrape.com/catalogue/'
    items = set()
    configured = False


    def parse(self, response):
        links = response.xpath("/html/body/div/div/div/div/section/div/ol/li/article/h3/a/@href").extract()
        if not self.configured and os.path.getsize('SITE_DATA.CSV') > 0:
            csv = pd.read_csv('SITE_DATA.CSV', usecols=["url"])
            self.items.update(csv['url'])
            self.configured = True
        for link in links:
                absolute_url = os.path.join(self.BASE_URL, link)
                if absolute_url not in self.items:
                    self.items.add(link)
                    yield scrapy.Request(absolute_url, callback=self.parse_attr)
        next_page = response.xpath('/html/body/div/div/div/div/section/div/div/ul/li/a/@href').extract()
        for next_page in next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_attr(self, response):
        item = Book()
        item["url"] = response.url
        item["title"] = "".join(response.xpath("/html/body/div/div/div/div/article/div/div/h1/text()").extract())
        item["description"] = "".join(response.xpath("/html/body/div/div/div/div/article/p/text()").extract())
        return item

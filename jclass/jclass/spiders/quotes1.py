# -*- coding: utf-8 -*-
import scrapy
from ..items import JclassItem


class Quotes1Spider(scrapy.Spider):
    name = 'quotes1'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):


        # item = JclassItem
        # quotes = response.xpath('//*[@class="text"]/text()').extract()
        # author = response.xpath('//*[@class="author"]/text()').extract()
        # tags = response.xpath('//*[@class="tag"]/text()').extract()

        all_divs = response.xpath('//*[@class="quote"]')
        for each_div in all_divs:
            quote = each_div.xpath('.//*[@class="text"]/text()').extract()
            author = each_div.xpath('.//*[@class="author"]/text()').extract()
            tags = each_div.xpath('.//*[@class="tag"]/text()').extract()

            items = JclassItem()
            items['quotes'] = quote
            items['author_names'] = author
            items['tags'] = tags

            yield items

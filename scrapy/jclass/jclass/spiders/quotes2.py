# -*- coding: utf-8 -*-
import scrapy
#Import Items
from ..items import JclassItem


class Quotes2Spider(scrapy.Spider):
    name = 'quotes2'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        
        #Instance of Item
        #items = JclassItem()
        
        quotes = response.xpath('//*[@class="text"]/text()').extract()
        authors = response.xpath('//*[@class="author"]/text()').extract()
        tags = response.xpath('//html/body/div[1]/div[2]/div[1]/div/div/a[1]/text()').extract()

        i = 0
        
        for quote in quotes:
            items = JclassItem()
            items['quotes'] = quote
            items['author_names'] = authors[i]
            items['tags'] = tags[i]
            i = i + 1
            yield items
        
        


# -*- coding: utf-8 -*-

import scrapy

class quoteBot(scrapy.Spider):
    name = "quoteBotTag"
    allowed_domains = ['www.quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com/']
    
    def parse(self, response):
        #Extracting the content using css selectors
        all_divs = response.css('div.quote')
        
        for quotes in all_divs:
            quoteName = quotes.css('span.text::text').extract()
            quoteBy = quotes.css('.author::text').extract()
            quoteTag = quotes.css('.tag::text').extract()
            yield {
                    'title': quoteName,
                    'Author': quoteBy,
                    'Tag': quoteTag
            }
       

        
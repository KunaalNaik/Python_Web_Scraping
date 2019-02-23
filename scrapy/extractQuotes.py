# -*- coding: utf-8 -*-

import scrapy

class quoteBot(scrapy.Spider):
    name = "quoteBot"
    allowed_domains = ['www.quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com/']
    
    def parse(self, response):
        #Extracting the content using css selectors
        
        
        quoteName = response.css('span.text::text').extract()
        quoteBy = response.css('small.author::text').extract()
       
        #Give the extracted content row wise
        for item in zip(quoteName,quoteBy):
            #create a dictionary to store the scraped info
            scraped_info = {
                'quoteName' : item[0],
                'quoteBy' : item[1],
            }

            #yield or give the scraped info to scrapy
            yield scraped_info
        
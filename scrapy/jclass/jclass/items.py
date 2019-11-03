# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JclassItem(scrapy.Item):
    # define the fields for your item here like:
    quotes = scrapy.Field()
    author_names = scrapy.Field()
    tags = scrapy.Field()
    

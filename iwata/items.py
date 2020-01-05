# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class IwataItem(scrapy.Item):
    title = scrapy.Field()
    heading = scrapy.Field()
    name = scrapy.Field()
    text = scrapy.Field()
    image = scrapy.Field()

    image_urls = scrapy.Field()
    images = scrapy.Field()

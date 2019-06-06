# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PttItem(scrapy.Item):
    push_userid = scrapy.Field()
    push_content = scrapy.Field()
    article_title = scrapy.Field()
    time = scrapy.Field()

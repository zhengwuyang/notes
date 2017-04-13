# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

#import scrapy
from scrapy.item import Item, Field


class AmazonItem(Item):
    # define the fields for your item here like:
    title = Field()
    price = Field()
    stars = Field()
    review = Field()
    asin = Field()
    url = Field()


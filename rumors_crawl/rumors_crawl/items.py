# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SnopeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    innerTitle = scrapy.Field()
    description = scrapy.Field()
    claim = scrapy.Field()
    claimReviewed = scrapy.Field()
    referredUrl = scrapy.Field()

class PolitifactItem(scrapy.Item):
    title = scrapy.Field()
    innerTitle = scrapy.Field()
    date = scrapy.Field()
    content = scrapy.Field()
    claimReviewed = scrapy.Field()
    referredUrl = scrapy.Field()

class ThoughcoItem(scrapy.Item):
    date = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    innerTitle = scrapy.Field()
    description = scrapy.Field()
    claim = scrapy.Field()
    claimReviewed = scrapy.Field()
    referredUrl = scrapy.Field()
    ciculatingSince = scrapy.Field()

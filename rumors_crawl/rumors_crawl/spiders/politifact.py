# -*- coding: utf-8 -*-
import scrapy


class PolitifactSpider(scrapy.Spider):
    name = 'politifact'
    allowed_domains = ['www.politifact.com']
    start_urls = ['http://www.politifact.com/']

    def parse(self, response):
        pass

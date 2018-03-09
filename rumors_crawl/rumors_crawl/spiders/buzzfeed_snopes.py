# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 15:05:15 2018

@author: prach
"""

import scrapy

class BuzzFeed(scrapy.Spider):
    name = "buzzfeed"
    allowed_domains = ['www.buzzfeed.com']

    def start_requests(self):
        url = 'https://www.buzzfeed.com/tag/rumors'
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        cards_ref = response.xpath('//div[contains(@class,"feed-cards")]//h2//parent::*/@href')
        for href in cards_ref.extract():
            if href is not None:
                yield response.follow(href, callback=self.parse_article)


    def parse_article(self,response):
        titleClass = response.xpath('//h1[contains(@class,"buzz-title")]/text()')
        date_time = response.xpath('//div[contains(@class,"buzz-timestamp")]')
        date_time2 = date_time.xpath('.//time[contains(@class,"buzz-timestamp__time")]/text()')
        content = response.xpath('//article//h3//text()')
        content_alt = response.xpath('//article//img//@alt')
        yield{
                'title': titleClass.extract_first(),
                'referred_url':response.request.url,
                'date': date_time2.extract_first(),
                'date2': date_time2.extract_first(),
                'content':''.join(content.extract()),
                'content_alt':''.join(content_alt.extract())
                }

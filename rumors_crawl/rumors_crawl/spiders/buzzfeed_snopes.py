# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 15:05:15 2018

@author: prach
"""

import scrapy

class BuzzFeed(scrapy.Spider):
    name = "buzzfeed"

    def start_requests(self):
        url = 'https://www.buzzfeed.com/tag/rumors'
      #  tag = getattr(self, 'tag', None)
       # if tag is not None:
        #    url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        feedCards = response.xpath('//div[contains(@class,"feed-cards")]')
    #    card_content = feedCards.xpath('.//div[contains(@class,"js-card__content")]')
        tag_line = feedCards.xpath('.//h2//parent::*/@href')
        
      #  feedCard = response.xpath('//div[contains(@class, "card story-card")]//div[contains(@class, "js-card__content")]//div[contains(@class,"xs-px05")]//a[contains(@class,"link-gray")]/@href')
  #      feedCard = response.xpath('//div[contains(@class, "card story-card")]//a[contains(@class,"link-gray")]/@href')
        for href in tag_line.extract():
            if href is not None:
                yield response.follow(href, callback=self.parse_article)


    def parse_article(self,response):
        titleClass = response.xpath('//h1[contains(@class,"buzz-title")]/text()')
        dateclass = response.xpath('//div[contains(@class,"buzz-timestamp")]')
        dateTime = dateclass.xpath('.//time[contains(@class,"buzz-timestamp__time")]/text()')
        yield{
                'title': titleClass.extract_first(),
                'date': dateTime.extract_first()
                }
        
        
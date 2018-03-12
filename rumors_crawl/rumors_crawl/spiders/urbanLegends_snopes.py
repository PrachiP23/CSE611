# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 15:05:15 2018

@author: prach
"""

import scrapy

class BuzzFeed(scrapy.Spider):
    name = "urbanLegends"

    def start_requests(self):
        url = 'https://www.thoughtco.com/urban-legends-4132595'
      #  tag = getattr(self, 'tag', None)
       # if tag is not None:
        #    url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        feedCards = response.xpath('//div[contains(@class,"loc content section-body")]//a/@href')

        for href in feedCards.extract():
        #    print(href)
            if href is not None:
                yield response.follow(href, callback=self.parse_article)


    def parse_article(self,response):
        details = response.xpath('//div[contains(@id,"flex_1-0")][1]/p[2]/text()')

        yield{
                'description': details.extract_first(),
                #'date': details[2].extract(),
                #'status': details[3].extract()
                }

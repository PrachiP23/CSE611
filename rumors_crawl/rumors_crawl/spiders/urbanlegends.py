# -*- coding: utf-8 -*-
from rumors_crawl.items import ThoughcoItem

import scrapy

class UrbanLegend(scrapy.Spider):
    name = "urbanlegends"

    def start_requests(self):
        url = 'https://www.thoughtco.com/urban-legends-in-the-news-4132594'
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        feedCards = response.xpath('//div[contains(@class,"section-body")]//li')

        for article in feedCards:
            href = article.xpath('./a/@href').extract_first()
            title = article.xpath('.//h2//text()').extract_first()
            item = ThoughcoItem(title=title)
            yield response.follow(href, callback=self.parse_article, meta={'item':item})


    def parse_article(self,response):
        item = response.meta['item']
        content = response.xpath('//div[contains(@class,"article-content")]//text()')
        innerTitle = response.xpath('//h1//text()')
        description = response.xpath('//h2/text()')
        date = response.xpath('//div[contains(@class,"article-updated-label")]//text()')
        claim = response.xpath('//div[contains(@class,"article-content")]/p[1]//text()')

        claimReviewed1 = response.xpath('//div[contains(@class,"article-content")]/p[2]/*[5]/text()').extract_first()
        claimReviewed2 = response.xpath('//div[contains(@class,"article-content")]/p[2]/*[5]/following-sibling::text()').extract_first()

        item['referredUrl'] = response.request.url
        item['content'] =  ''.join(content.extract()),
        item['innerTitle'] = innerTitle.extract_first(),
        item['description'] = description.extract_first(),
        item['date'] = date.extract_first(),
        item['claim'] = claim.extract_first(),
        item['claimReviewed'] = ''.join(filter(None,(claimReviewed1,claimReviewed2)))
        yield item

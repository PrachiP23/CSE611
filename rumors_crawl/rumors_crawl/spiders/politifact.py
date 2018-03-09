import scrapy
from rumors_crawl.items import PolitifactItem


class PolitifactSpider(scrapy.Spider):
    name = 'politifact'
    allowed_domains = ['www.politifact.com']
    start_urls = ['http://www.politifact.com/punditfact/statements/']

    def parse(self, response):
        rumors = response.xpath('//section[@class="scoretable"]/div')
        for rumor in rumors:
            title = ''.join(rumor.xpath('.//p[@class="statement__text"]//text()').extract())
            claimReviewed = rumor.xpath('.//div[@class="meter"]/p//text()').extract_first()

            article_page = rumor.xpath('.//p[@class="statement__text"]/a/@href').extract_first()
            item = PolitifactItem(title=title, claimReviewed=claimReviewed)
            yield response.follow(article_page, callback=self.parse_article, meta={'item':item})

    def parse_article(self, response):
        item = response.meta['item']
        item["referredUrl"] = response.request.url,
        item["innerTitle"] = response.xpath('//h1[@class="article__title"]//text()').extract_first()
        item["date"] = response.xpath('//p[@class="article__meta"]//span//text()').extract_first()
        item["content"] = ''.join(response.xpath('//div[@class="article__text"]//text()').extract())

        yield item

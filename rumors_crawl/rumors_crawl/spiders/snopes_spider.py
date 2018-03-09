import scrapy
from rumors_crawl.items import SnopeItem

class SnopesSpider(scrapy.Spider):

    name="snopes"
    start_urls=['https://www.snopes.com/50-hottest-urban-legends/']

    def parse(self, response):

        articles = response.xpath("//div[@id='main-list']//article")
        for article in articles:
            item = SnopeItem(
            date=article.xpath('.//span[@class="article-date"]/text()').extract_first(),
            title=article.xpath('.//h2[@class="title"]/text()').extract_first())

            article_page = article.xpath('.//a/@href').extract_first()

            yield response.follow(article_page, callback=self.parse_article, meta={'item':item})
            #request.meta['item'] = item
            #return request

    def parse_article(self, response):
        item = response.meta['item']
        article = response.xpath('//div[contains(@class,"article-text")]')

        item["referredUrl"] = response.request.url,
        item['innerTitle']=response.xpath('//h1/text()').extract_first()
        item['description']=response.xpath('//h2/text()').extract_first()
        item['claim']=article.xpath('.//p[@itemprop="claimReviewed"]//text()').extract_first()
        item['claimReviewed']=article.xpath('..//div[contains(@class,"claim")]/span/text()').extract_first()
        item['content'] = ''.join(article.xpath('./*[self::p or self::blockquote or self::article]//text()').extract())
        yield item
#//div[contains(@class,"article-text")]//*[self::p or self::blockquote]//text()

import scrapy

class SnopesSpider(scrapy.Spider):

    name="snopes"
    start_urls=['https://www.snopes.com/50-hottest-urban-legends/']

    def parse(self, response):
        articles = response.xpath("//div[@id='main-list']//article")
        for article in articles:
            yield {
                'date': article.xpath('.//span[@class="article-date"]/text()').extract_first(),
                'title': article.xpath('.//h2[@class="title"]/text()').extract_first()
            }

            article_page = article.xpath('.//a/@href').extract_first()

            yield response.follow(article_page, callback=self.parse_article)


    def parse_article(self, response):
        article = response.xpath('//div[contains(@class,"article-text")]')

        yield {
            'title':response.xpath('//h1/text()').extract_first(),
            'description':response.xpath('//h2/text()').extract_first(),
            'claim':article.xpath('.//p[@itemprop="claimReviewed"]//text()').extract_first(),
            'claimReviewed':article.xpath('..//div[contains(@class,"claim")]/span/text()').extract_first(),
        }
        #content = article.xpath('./*[self::p or self::blockquote]//text()')
        #for info in content:
        #    info.extract_first()

import scrapy

class SnopesSpider(scrapy.Spider):

    name="snopes"
    start_urls=['https://www.snopes.com/50-hottest-urban-legends/']

    def parse(self, response):
        articles = response.xpath("//div[@id='main-list']//div[@class='article-link-container']")
        for article in articles:
            yield {
                'date': article.xpath('.//span[@class="article-date"]/text()').extract_first(),
                'title': article.xpath('.//h2[@class="title"]/text()').extract_first()
            }

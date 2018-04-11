import scrapy
#from scrapy.exceptions import CloseSpider

class Breitbart(scrapy.Spider):

    name="breitbart"
    start_urls=['http://www.breitbart.com/']

    def parse(self, response):

        articles = response.xpath('//article/h2/a/@href | //div[@id="BBTrendNow"]/ul/li/a/@href')

        for href in articles.extract():
            if href is not None:
                yield response.follow(href, callback=self.parse_article)


    def parse_article(self,response):
        article_info = response.xpath('//div[@id="MainW"]/article')
        titleClass = article_info.xpath('./header/h1/text()')
        date_time = article_info.xpath('./header/p/span[2]/text()')
        content = article_info.xpath('./div/h2/text() | ./div/p/text()')
        yield{
                'title': titleClass.extract_first(),
                'referred_url':response.request.url,
                'date': date_time.extract_first(),
                'content':''.join(content.extract()),
                }

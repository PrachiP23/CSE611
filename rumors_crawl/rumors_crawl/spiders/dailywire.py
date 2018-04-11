import scrapy
#from scrapy.exceptions import CloseSpider

class DailyWire(scrapy.Spider):

    name="dailyWire"
    start_urls=['https://www.dailywire.com/']

    def parse(self, response):

        articles = response.xpath("//article/div/a/@href")

        for href in articles.extract():
            if href is not None:
                yield response.follow(href, callback=self.parse_article)


    def parse_article(self,response):
        titleClass = response.xpath('//article/header/h1')
        date_time = response.xpath('//div[contains(@class,"byline")]/div/time')
        content = response.xpath('//div[contains(@class, "field-body")]/p/text()')
        yield{
                'title': titleClass.extract_first(),
                'referred_url':response.request.url,
                'date': date_time.extract_first(),
                'content':''.join(content.extract()),
                }

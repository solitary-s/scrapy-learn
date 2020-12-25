import scrapy


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['login.com\']
    start_urls = ['http://login.com\/']

    def parse(self, response):
        pass

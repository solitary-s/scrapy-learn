import scrapy
from scrapy.http import Request, FormRequest

class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['e-lead.cn', 'test3.e-lead.cn', 'itest.e-lead.cn']

    start_urls = ['http://itest.e-lead.cn/oa/index']

    def parse(self, response):
        name = response.css('div.info1').xpath('./div/text()')
        yield {'name': name}

    login_page = 'http://test3.e-lead.cn:8090/sso/oauth/authorize?response_type=code&client_id=elead_oa&redirect_uri=http%3A%2F%2Fitest.e-lead.cn%2Foa%2FcodeCallback%3Fredirect_uri%3D%252Findex'
    # login_url = 'http://test3.e-lead.cn:8090/sso/oauth/authorize?response_type=code&client_id=elead_oa&redirect_uri=http%3A%2F%2Fitest.e-lead.cn%2Foa%2FcodeCallback%3Fredirect_uri%3D%252Findex'

    def start_requests(self):
        yield scrapy.Request(self.login_page, callback=self.login)

    def login(self, response):
        fd = {'username': '3568', 'password': '123456'}
        yield FormRequest.from_response(response, formdata=fd, callable=self.parse)

import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import FilesItem

class FilesSpider(scrapy.Spider):
    name = 'files'
    allowed_domains = ['matplotlib.org']
    start_urls = ['http://matplotlib.org/examples/index.html']

    def parse(self, response):
        le = LinkExtractor(restrict_css='div.toctree-wrapper.compound li', deny='/index.html$')
        print(len(le.extract_links(response)))
        print('le --------- %s' % le)
        for link in le.extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse_file)

    def parse_file(self, response):
        href = response.css('a.reference.internal::attr(href)').extract()[0]
        url = response.urljoin(href)
        files = FilesItem()
        files['file_urls'] = [url]
        return files

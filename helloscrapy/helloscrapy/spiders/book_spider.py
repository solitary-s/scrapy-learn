import scrapy
from ..items import BookItem
from scrapy.linkextractors import LinkExtractor

class BooksSpider(scrapy.Spider):
    name = "books"

    start_urls = ['http://books.toscrape.com/']

    def parse(self, response, **kwargs):
        for book in response.css('article.product_pod'):
            item = BookItem()
            item['name'] = book.xpath('./h3/a/@title').extract_first()
            item['price'] = book.css('p.price_color::text').extract_first()
            yield item

        # next_url = response.css('ul.pager li.next a::attr(href)').extract()[0]
        # print('next_url------- : %s' % next_url)
        # if next_url:
        #     next_url = response.urljoin(next_url)
        #     yield scrapy.Request(next_url, callback=self.parse)
        le = LinkExtractor(restrict_css='ul.pager li.next')
        links = le.extract_links(response)
        if links:
            next_url = links[0].url
            yield scrapy.Request(next_url, callback=self.parse)












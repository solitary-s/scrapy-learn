import scrapy
import json
from ..items import SoImageItem
from scrapy.pipelines.images import ImagesPipeline

class ImagesSpider(scrapy.Spider):

    BASE_URL = 'https://image.so.com/zjl?ch=art&sn=%s&listtype=new&temp=1'
    start_index = 0

    MAX_DOWNLOAD_NUM = 1000

    name = 'images'
    allowed_domains = ['image.so.com']
    start_urls = [BASE_URL % 0]

    def parse(self, response):
        infos = json.loads(response.body.decode('utf-8'))
        image = SoImageItem()
        image['image_urls'] = [info['qhimg_url'] for info in infos['list']]
        yield image

        self.start_index += infos['count']
        if infos['count'] > 0 and self.start_index < self.MAX_DOWNLOAD_NUM:
            yield scrapy.Request(self.BASE_URL % self.start_index)

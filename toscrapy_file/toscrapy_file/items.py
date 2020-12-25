# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ToscrapyFileItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class FilesItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()


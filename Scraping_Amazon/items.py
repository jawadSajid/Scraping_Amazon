# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapingamazonItem(scrapy.Item):
    # define the fields for your item here like:
    product_name = scrapy.Field()
    author = scrapy.Field()
    price = scrapy.Field()
    product_image_link = scrapy.Field()
    pass

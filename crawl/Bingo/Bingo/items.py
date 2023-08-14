# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BingoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MoveItem(scrapy.Item):
    # 电影名字
    title = scrapy.Field()
    # subject
    subject = scrapy.Field()
    # 评分
    score = scrapy.Field()

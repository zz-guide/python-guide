import scrapy
from scrapy import Selector

from Bingo.items import MoveItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250']

    def parse(self, response, *args, **kwargs):
        se = Selector(response)
        list_items = se.css('#content > div > div.article > ol > li')
        for item in list_items:
            move_item = MoveItem()
            move_item['title'] = item.css('span.title::text').extract_first()
            move_item['subject'] = item.css('span.inq::text').extract_first()
            move_item['score'] = item.css('span.rating_num::text').extract_first()
            yield move_item

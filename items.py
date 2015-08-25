import scrapy

class AnimeItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()

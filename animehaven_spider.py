import scrapy

from items import AnimeItem

class DmozSpider(scrapy.Spider):
    name = "animehaven"
    allowed_domains = ["animehaven.org"]
    start_urls = [
        "http://animehaven.org/"
    ]

    def parse(self, response):
        for anchor in response.css(".category_alphabet_title_link"):
            item = AnimeItem()
            item['title'] = anchor.xpath('text()').extract()
            item['link'] = anchor.xpath('@href').extract()
            yield item
            # yield scrapy.Request(url, callback=self.parse_contents)

    # def parse_contents(self, response):
        # Do stuff

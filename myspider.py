import scrapy

class BlogSpider(scrapy.Spider):
    def start_requests(self):
        start_urls = ['https://ivcevidensia.co.uk']
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response.url)
import scrapy


class BlackspiderSpider(scrapy.Spider):
    name = "blackspider"
    allowed_domains = ["www.blackrock.com"]
    start_urls = ["https://www.blackrock.com/us/financial-professionals/investment-strategies/bitcoin-investing"]

    def parse(self, response):
        pass

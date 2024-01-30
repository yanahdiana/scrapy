import scrapy


class ValkyspiderSpider(scrapy.Spider):
    name = "valkyspider"
    allowed_domains = ["valkyrieinvest.com"]
    start_urls = ["https://valkyrieinvest.com/brrr/"]

    def parse(self, response):
       nb_bitcoin = response.css('.mcb-column-inner-jm3z2by6 > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(3)::text').get()
       nb_bitcoin = nb_bitcoin.replace(',','')
       nb_bitcoin = float(nb_bitcoin)
       
       yield {
           
           'name' : 'Valkyrie Bitcoin Fund',
           'ticker' : 'BRRR',
           'nb_bitcoin' : nb_bitcoin
           
       }
       
       
       
        

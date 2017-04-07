import scrapy


class ExchangeRateSpider(scrapy.Spider):
    name = "exchange_rate"

    start_urls = [
        'https://www.mbank.pl/serwis-ekonomiczny/kursy-walut/',
    ]

    def parse(self, response):
        for row in response.xpath('//div[@class="table_0"]/table[@class="default"]/tbody/tr'):
            if self.check_if_eur(row) or self.check_if_usd(row):
                yield self.get_context(row)

    def get_context(self, selector):
        return {
            "currency": selector.xpath('./td[@class="unit"]/div/text()').extract_first(),
            "buy": selector.xpath('./td[5]/text()').extract_first(),
            "sell": selector.xpath('./td[6]/text()').extract_first(),
            "average": selector.xpath('./td[7]/text()').extract_first(),
        }

    def check_if_usd(self, row):
        return True if row.xpath('./td[@class="unit"]/div/text()').extract_first() == 'USD' else False

    def check_if_eur(self, row):
        return True if row.xpath('./td[@class="unit"]/div/text()').extract_first() == 'EUR' else False

from exchange_rate.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, MAIL_FROM, MAIL_TO
from scrapy import signals


class ExchangeRatePipeline(object):
    def __init__(self):
        self.files = {}
        self.rate = "Subject: Raport - kurs walut\n"

    @classmethod
    def from_crawler(cls, crawler):
        spider = cls()
        crawler.signals.connect(spider.spider_closed, signals.spider_closed)
        return spider

    def spider_closed(self, spider):
        import smtplib
        smtpObj = smtplib.SMTP("smtp.gmail.com", "587")
        smtpObj.starttls()
        smtpObj.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        smtpObj.sendmail(MAIL_FROM, MAIL_TO, self.rate)

    def process_item(self, item, spider):
        self.rate += '{} kupno {} sprzedaz {} srednia {}\n'.format(item['currency'], item['buy'], item['sell'],
                                                                   item['average'])
        return item

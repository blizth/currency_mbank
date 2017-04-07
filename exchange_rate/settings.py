import os

BOT_NAME = 'exchange_rate'

SPIDER_MODULES = ['exchange_rate.spiders']
NEWSPIDER_MODULE = 'exchange_rate.spiders'

EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

MAIL_FROM = ""
MAIL_TO = ["", ]

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'exchange_rate.pipelines.ExchangeRatePipeline': 300,
}

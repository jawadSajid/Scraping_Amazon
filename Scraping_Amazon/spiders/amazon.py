import scrapy
from ..items import ScrapingamazonItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        'https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&fst=as%3Aoff&qid'
        '=1595477787&rnid=1250225011&ref=lp_283155_nr_p_n_publication_date_0 '
    ]

    def parse(self, response):
        items = ScrapingamazonItem()

        product_name = response.css()
        author = response.css()
        price = response.css()
        product_image_link = response.css()

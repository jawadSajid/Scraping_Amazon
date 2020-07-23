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

        product_name = response.css(".a-color-base.a-text-normal::text").extract()
        author = response.css(".a-color-base .a-size-base+ .a-size-base::text").extract()
        price = response.css(".a-spacing-top-small .a-price-whole , .a-spacing-top-small .a-price-fraction").css("::text").extract()
        product_image_link = response.css(".s-image").xpath("@src").extract()

        items['product_name'] = product_name
        items['author'] = author
        items['price'] = price
        items['product_image_link'] = product_image_link

        yield items

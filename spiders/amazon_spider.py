# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazontutorialItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    page_number = 3
    allowed_domains = ['jd.com']
    start_urls = [
        'https://search.jd.com/Search?keyword=macbook&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&bs=1&suggest=1.his.0.0&ev=exbrand_Apple%5E&page=1&s=1&click=0']

    def parse(self, response):
        items = AmazontutorialItem()
        div_products = response.css('.gl-i-wrap')
        for product in div_products:
            product_name = product.css('.p-name-type-2 em::text ').extract()
            # product_year = product.css('.p-name-type-2 em::text ').extract()
            product_price = product.css('.p-price i::text').extract()

            items['product_name'] = product_name[1]
            # items['product_year'] = product_year[1]
            items['product_price'] = product_price[0]

            yield items
        next_page = 'https://search.jd.com/Search?keyword=macbook&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&bs=1&suggest=1.his.0.0&ev=exbrand_Apple%5E&page=' + str(
            AmazonSpiderSpider.page_number) + '&s=1&click=0'
        while AmazonSpiderSpider.page_number <= 5:
            yield response.follow(next_page, callback=self.parse)
            AmazonSpiderSpider.page_number += 2

# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/random']

    def parse(self, response):
        self.log('---------------------------' + response.url)
        yield {
            'author_name': response.css('small.author::text').extract_first(),
            'test': response.css('span.text::text').extract_first(),
            'tags': response.css('a.tag::text').extract_first(),
        }

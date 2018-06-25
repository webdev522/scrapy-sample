# -*- coding: utf-8 -*-
import scrapy


class AuthorsSpider(scrapy.Spider):
  name = 'authors'
  allowed_domains = ['toscrape.com']
  start_urls = ['http://quotes.toscrape.com']

  def parse(self, response):
    self.log('---------------------------' + response.url)
    urls = response.css('div.quote > span > a::attr(href)').extract()

    for url in urls:
      url = response.urljoin(url)
      yield scrapy.Request(url=url, callback=self.parse_details)
      
      # pagination link
      next_page_url = response.css('li.next > a::attr(href)').extract_first()
      if next_page_url:
        next_page_url = response.urljoin(next_page_url)
        yield scrapy.Request(url=next_page_url, callback=self.parse)

  def parse_details(self, response):
    yield {
      'name': response.css('h3.author-title::text').extract_first(),
      'birth_date': response.css('span.author-born-date::text').extract_first()
    }
    
       
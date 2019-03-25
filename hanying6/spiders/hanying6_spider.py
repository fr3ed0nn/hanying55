# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector
from hanying6.items import Hanying6Item
from scrapy.conf import settings

class Hanying6Spider(Spider):
	name = "hanying6"
	allowed_domains = ["hanying6.com"]
	start_urls = (
		'https://www.baidu.com/',
	)

	def start_requests(self):
		reqs = []
		for m in range(1,211):
			url = 'http://hanying6.com/page/%s'%(m,)
				
			req = scrapy.Request(url, headers={'Referer':'http://www.google.com'})
			reqs.append(req)
		return reqs

	def parse(self, response):		
		for sel in response.xpath("//ul[@id='post_container']//h2/a"):
			url = sel.xpath('@href').extract()[0]
			print(url)
			yield scrapy.Request(url, callback=self.parse_detail)
	
	def parse_detail(self, response):
		item = Hanying6Item()
		item['moviename'] = response.xpath("//h1/text()").extract()[0]
		item['torrenturl'] = response.xpath("//span[@class='torrent']//a/@href").extract()
		yield item
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.conf import settings
import re

class StorePipeline(object):
	def process_item(self, item, spider):
		filename = 'res.txt'
		text = item['moviename'].split('/')[0] + ', ' + str(item['torrenturl']) + '\n'
		fp = open(filename, 'a+')
		fp.write(text)
		fp.close()
		
		return item
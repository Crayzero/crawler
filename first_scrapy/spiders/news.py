# encoding: utf-8

from scrapy.spider import Spider
from scrapy.selector import Selector
import re
from first_scrapy.items import NewsItem

class NewsSpider(Spider):
	"""
	docstring for NewsSpider
	scrab infromation from http://news.dbanotes.net/
	"""
	name='startupnews'
	allowed_domains=['news.dbanotes.net']
	start_urls=['http://news.dbanotes.net',]
	base=start_urls[0]
	def parse(self,response):
		self.log('%s be crawled.'%response.url)
		sel=Selector(response)
		newss=sel.xpath('//td[@class="title"]/a')
		log_file=open('a.txt','a+')
		requests=[]
		for news in newss:
			title=news.xpath('text()').extract()
			link=news.xpath('@href').extract()
			if title and link:
				item=NewsItem()
				item['title']=title[0]
				item['link']=link[0]
				a=u'%s,%s\n'%(title[0],link[0])
				#print a
				log_file.write(a.encode('utf-8'))
				yield item
				if title[0]=='More':
					url=self.base+link[0]
					yield self.make_requests_from_url(url)
#或者可以返回一个scrapy.http.Request的对象，使用方法为：Request(url,callback='xxx')
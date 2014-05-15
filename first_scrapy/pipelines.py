# -*- coding:utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy import log
from twisted.enterprise import adbapi
from scrapy.http import Request
from scrapy.exceptions import DropItem
from first_scrapy.items import NewsItem
import time
import MySQLdb
import MySQLdb.cursors
class FirstScrapyPipeline(object):
    def process_item(self, item, spider):
        return item


class StartupNews(object):
	"""docstring for StartupNews"""
	def __init__(self):
		self.dbpool=adbapi.ConnectionPool('MySQLdb',
			host='127.0.0.1',
			db='startupnews',
			user='root',
			passwd='111111',
			cursorclass=MySQLdb.cursors.DictCursor,
			charset='utf8',
			use_unicode=True
			)
	def process_item(self,item,spider):
		query=self.dbpool.runInteraction(self._insert,item)
		query.addErrback(self.handle_error)

	def _insert(self,tx,item):
		if item.get('title'):
			#print item['title'],item['link']  insert into titles values ("我擦","doubi")
			query="insert into sites values(\"%s\",\"%s\")"%(item['title'],item['link'])
			print query
			tx.execute(query)

	def handle_error(self,e):
		log.err(e)
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class FirstScrapyItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass

class DmozItem(Item):
	"""Dmoz Item is a test Item from the doc of scrapy:
	http://doc.scrapy.org/en/latest/intro/tutorial.html
	"""
	title=Field()
	link=Field()
	desc=Field()

class NewsItem(Item):
	"""docstring for News"""
	title=Field()
	link=Field()
		
# -*- coding: utf-8 -*-
#!/usr/bin/env python
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from ..items import HackernewsscraperItem

class HackerNewsScraper(BaseSpider):
	name = 'hacker'
	start_urls = ['https://news.ycombinator.com/']

	def parse(self, response):
		selector = Selector(response)
		news_titles = selector.xpath("//td[@class='title']")
		selections = []

		for data in news_titles:
			selection = HackernewsscraperItem()
			selection['title'] = data.xpath("a/text()").extract()
			selection['link'] = data.xpath("a/@href").extract()
			selections.append(selection)

		return selections
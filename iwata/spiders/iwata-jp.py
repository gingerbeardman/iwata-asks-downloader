#!/usr/bin/python

# CodeRunner run command
# cd ../../; rm iwata-jp.jl; scrapy crawl iwata-jp -o iwata-jp.jl

## Iwata Asks (JP) Item

import scrapy
import logging

class IwataSpider(scrapy.Spider):
	name = 'iwata-jp'

	start_urls = [
		'https://www.nintendo.co.jp/wii/interview/rmcj/vol1/index.html',
#		'https://www.nintendo.co.jp/wii/interview/rmcj/vol1/index5.html',
	]

	def parse(self, response):
#		for heading in response.css('h3'):
#			yield {'heading': heading.css('img::attr(alt)').get()}

		for row in response.css('div#int-box-wrap > div:not(.clear), h3'):
			yield {
				'heading': row.css('img::attr(alt)').extract(),
				'name': row.css('div.int-name p::text').extract(),
				'text': row.css('div.int-text p::text').extract(),
				'notes_num': row.css('div.notes-num p::text').extract(),
				'notes_text': row.css('div.notes-text p::text').extract(),
				'image': row.css('div > img').xpath('@src').extract(),
			}

#		next_page = response.css('div#page-next a::attr(href)').get()
#		if next_page is not None:
#			yield response.follow(next_page, self.parse)
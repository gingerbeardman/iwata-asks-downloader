#!/usr/bin/python

# CodeRunner run command
# cd ../../; rm iwata-eu.jl; scrapy crawl iwata-eu -o iwata-eu.jl

## Iwata Asks (EU) Item

import scrapy

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from iwata.items import IwataItem
from w3lib.html import remove_tags, replace_escape_chars

#import logging
#logger = logging.getLogger()
#logger.setLevel(logging.DEBUG)

class IwataSpider(scrapy.Spider):
	name = "iwata-eu"

#	start_urls = [
#		"https://www.nintendo.co.uk/Iwata-Asks/Iwata-Asks-Mario-Kart-Wii/Bringing-Racers-Together/1-It-Started-With-A-Guy-In-Overalls/1-It-Started-With-A-Guy-In-Overalls-214509.html",
#	]

	def __init__(self, name=None, **kwargs):
			if 'start_urls' in kwargs:
				self.start_urls = kwargs.pop('start_urls').split(',')
			super(IwataSpider, self).__init__(name, **kwargs)

	def parse(self, response):
		loader = ItemLoader(item=IwataItem(), response=response)
		loader.add_css("title", "ul.breadcrumb li:nth-child(3) a::text")
		loader.add_css("title", "ul.breadcrumb li:nth-child(4) a::text")
		yield loader.load_item()

		loader = ItemLoader(item=IwataItem(), response=response)
		loader.add_css("heading", "div.instapaper_body h1::text")
		yield loader.load_item()

		for row in response.css("div.instapaper_body > div.row"):
			loader = ItemLoader(item=IwataItem(), selector=row, response=response)

			loader.default_input_processor = MapCompose(replace_escape_chars)
			loader.default_output_processor = TakeFirst()

			loader.add_css("name", "div.interviewer_name span::text")
			loader.add_css("text", "div.interviewer_text p")
			loader.add_css("image", "img.img-responsive::attr('src')")
			yield loader.load_item()


		images = IwataItem()
		relative_img_urls = response.css("div.instapaper_body > div.row img.img-responsive::attr('src')").extract()
		images["image_urls"] = self.url_join(relative_img_urls, response)
		yield images
		
		next_page = response.css("div.nextPage a.arrow_right::attr('href')").get()
		if next_page is not None:
			yield response.follow(next_page, self.parse)

	def url_join(self, urls, response):
		joined_urls = []
		for url in urls:
			joined_urls.append(response.urljoin(url))

		return joined_urls

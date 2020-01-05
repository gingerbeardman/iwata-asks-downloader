# Iwata Asks Downloader

This tool downloads the Iwata Asks series of interviews, saving as Markdown and HTML with images.

I created this tool in Spring/Summer 2019 so that I could more easily read and search the Iwata Asks interviews.

_Note: This tool was developed and tested on macOS, so  I'm not sure how/if it works on Windows/Linux._

## Fund Development

You can fund development of this tool, or just say thanks, through one of the following:

- Patreon: [https://www.patreon.com/gingerbeardman/](https://www.patreon.com/gingerbeardman/)
- Ko-Fi: [https://ko-fi.com/gingerbeardman](https://ko-fi.com/gingerbeardman)
- PayPal: [https://www.paypal.me/mattsephton](https://www.paypal.me/mattsephton)

Your support is appreciated!

## Copyright Notice

- _None of the Iwata Asks interview content is stored here!_
- The Iwata Asks interview content remains copyright of its creators.
- This tool and its output is meant for personal use only. 
- Don't do anything you shouldn't do with the content.
- Watch out for the Ninjas!

## Prerequisites 

- Python (2 or 3) with
  - [pip](https://pip.pypa.io/en/stable/installing/) (see [here](https://pip.pypa.io/en/stable/installing/)) which may require Xcode Command-line Tools (`$ xcode-select --install`)
  - [markdown](https://python-markdown.github.io/install/) (`$ python -m pip install markdown`)
  - [jinja](https://pypi.org/project/Jinja2/) (`$ python -m pip install jinja2`)
  - [PIL](https://pillow.readthedocs.io/en/stable/installation.html) (`$ python -m pip install Pillow`)
- [Scrapy](https://scrapy.org) (`$ pip install scrapy`)

Note: Catalina users will need to add `--user` to the end of each python pip command

## Usage

1. Run the scraper using the script as follows: `./get_all.sh iwata-eu.csv`
1. Wait a while for the process to complete (approx. 25 minutes on first run)
1. Output is placed in the `_md`, `_html` and `_images` folders

## How does this work?

[Scrapy](https://scrapy.org) is a framework for creating web spiders. 

A web spider loads a web page and extracts content from it according to defined rules/logic/programming.

This tool uses a list of URLs for the first page of each interview (`iwata-eu.csv`) to feed the scraper, whose web spider (`iwata-eu.py`) extracts the content and automatically includes subsequent pages by following the original page navigation links. The main loop process is controlled by a shell script (`get_all.sh`).

Currently the scraper only works on the EU series of interviews due to their static page structure being more suitable (the USA interviews use AJAX to load content). The EU list has around 200 seed URLs, most of which have multiple pages, and download and processing of over 30,000 files takes quite a while the first time (approx. 25 minutes). Subsequent runs will used cached data and will be quicker (appox. 13 minutes). The result is around 180 Markdown/HTML files.

The scraper parses out the following content:
- Page Title (`title`)
- Section Heading (`heading`)
- Interviewer Name (`name`)
- Interviewer Text (`text`)
- Related Image (`image`)

The content from multiple pages is processed and reformatted, as Markdown and HTML, and finally saved to disk as a single file.

Note: HTML generation accounts for approx. 3 minutes of processing time.

## Development Setup

You'll need to familiarise yourself with [Scrapy](https://scrapy.org) and go through their [tutorial](http://docs.scrapy.org/en/latest/intro/overview.html) before diving in.

Important files:
- `/iwata-eu.csv` (list of seed URLs)
- `/iwata/` (folder)
- `/iwata/pipelines.py` (pipeline definitions)
- `/iwata/settings.py` (settings, including debug pipelines)
- `/iwata/spiders/` (folder)
- `/iwata/spiders/iwata-eu.py` (the most important file, the spider itself!)

Notes
- You'll see notes about command lines used to test the spider that I use in the CodeRunner app, but you should be able to use them on the command line too. 
- Scrapy caches content in `/.scrapy/httpcache` so you can develop using a cache of the pages rather than wait for downloading each time.
- I recommend developing using a subset of pages and only use the full list (`iwata-eu.csv`) for your final output. 

## Contributions

I will happily accept and merge any PR that improves this tool. I wrote this as I learned about Scrapy so there is undoubtedly room for improvement. Contributions are very welcome!

- Optimisation that speed up any part of the processing
- Improvements to readable output
- Improvements to format conversion
- Adding missing interviews (each source will require a new spider)
- Add/check support for Windows/Linux
- Improvements to `README.md`

## To Do 

- Convert to single EPUB with chapters (using pandoc?)
- Japan-only interviews (work begun, see `iwata-jp.py`)
- Fan translations of Japan-only interviews (see [here](http://www.nintendoworldreport.com/tag/43407/iwata-asks-in-commemoration), [here](https://gameinjapanese.com/translations/), [here](https://kamedani.tumblr.com/archive))
- SNES Classic developer interviews (see [here](https://www.nintendo.com/super-nes-classic/))
- USA-only interviews (see [interviews.xml](https://iwataasks.nintendo.com/_ui/xml/interviews.xml))
- Video interviews (thumbnail and link? see `iwata-eu-video.csv`)
- Any other interviews (see [Wikipedia](https://en.wikipedia.org/wiki/List_of_Iwata_Asks_interviews))

## Changelog

* `2020-01-05`: public release
* `2019-07-03`: support for multiple pages
* `2019-06-22`: continued improvements
* `2019-04-15`: initial scraper and spider

## Licence

[MIT](LICENSE)

## Screenshots

Online vs Local

![Online](screengrab_online.png) ![Local](screengrab_local.png)
#!/bin/bash

rm ./_md/*.md
rm ./_html/*.html
while read url
do
	scrapy crawl -a start_urls=$url iwata-eu
done < "$@"

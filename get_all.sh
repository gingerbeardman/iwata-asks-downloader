#!/bin/bash

[[ "$(python -V)" =~ "Python 3" ]] || echo "Iwata Asks Downloader: please make sure Python 3 is installed as default" || exit;

rm ./_md/*.md
rm ./_html/*.html
while read url
do
	scrapy crawl -a start_urls=$url iwata-eu
done < "$@"

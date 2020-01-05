#!/bin/bash

rm ./_md/*.md
rm ./_html/*.html
while read url
do
	scrapy crawl -a start_urls=$url iwata-eu
done < "$@"

#cd _html
#pandoc -o "Iwata Asks.epub" --toc --toc-depth=1 --metadata-file=meta/metadata.yaml --css=css/iwata.css \
#       -i "html/*.html"
#open "Iwata Asks.epub"
#cd ..

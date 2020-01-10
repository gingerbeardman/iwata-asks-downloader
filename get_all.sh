#!/bin/bash

echo "IWATA ASKS DOWNLOADER by @gingerbeardman"
echo

[[ "$(python -V)" =~ "Python 3" ]] || echo "Please make sure Python 3 is installed as default" || exit;

rm ./_md/*.md &> /dev/null
rm ./_html/*.html &> /dev/null

echo "Downloading and processing web pages..."
total=`wc -l < $1`
while read platform url
do
	let "n+=1"
	python ./progress.py ${n} ${total} 40
	scrapy crawl -a start_urls=$url iwata-eu &> /dev/null
done < "$@"
echo

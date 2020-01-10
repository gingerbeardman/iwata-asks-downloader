#!/bin/bash
start=$SECONDS

printf "IWATA ASKS DOWNLOADER by @gingerbeardman\n\n"

[[ "$(python -V)" =~ "Python 3" ]] || echo "Please make sure Python 3 is installed as default" || exit;

rm ./_md/*.md &> /dev/null
rm ./_html/*.html &> /dev/null

printf "Downloading and processing web pages...\n"
total=`wc -l < $1`
while read platform url
do
	let "n+=1"
	python ./progress.py ${n} ${total} 40
	scrapy crawl -a start_urls=$url iwata-eu &> /dev/null
done < "$@"

end=$SECONDS
printf "\n\nTime taken: $((($end-$start)/60)) minutes\n"

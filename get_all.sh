#!/bin/bash

echo "IWATA ASKS DOWNLOADER by Matt Sephton @gingerbeardman"

[[ "$(python -V)" =~ "Python 3" ]] || echo "Please make sure Python 3 is installed as default" || exit;

# https://github.com/fearside/ProgressBar
function ProgressBar {
    let _progress=(${1}*100/${2}*100)/100
    let _done=(${_progress}*4)/10
    let _left=40-$_done
    _fill=$(printf "%${_done}s")
    _empty=$(printf "%${_left}s")
	printf "\rProgress : [${_fill// /#}${_empty// /-}] ${_progress}%%"
}

rm ./_md/*.md &> /dev/null
rm ./_html/*.html &> /dev/null

total=`wc -l < $1`
while read platform url
do
	let "n+=1"
	ProgressBar ${n} ${total}
	scrapy crawl -a start_urls=$url iwata-eu &> /dev/null
done < "$@"

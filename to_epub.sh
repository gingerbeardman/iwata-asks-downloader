#!/bin/bash

echo "IWATA ASKS DOWNLOADER by @gingerbeardman"
echo

rm ./_epub/*.epub

echo "Generating EPUB files..."
cd _html
total=`ls *.html | wc -l`
for f in *.html
do
	let "n+=1"
	python ../progress.py ${n} ${total} 40
	pandoc "${f}" --toc --toc-depth=1 --metadata-file=meta/metadata.yaml --css=css/epub.css -o "../_epub/${f%.html}.epub"
done
echo
cd ..

#!/bin/bash
start=$SECONDS

printf "IWATA ASKS DOWNLOADER by @gingerbeardman\n\n"

rm ./_epub/*.epub

printf "Generating EPUB files...\n"
cd _html
total=`ls *.html | wc -l`
for f in *.html
do
	let "n+=1"
	python ../progress.py ${n} ${total} 40
	pandoc "${f}" --toc --toc-depth=1 --metadata-file=meta/metadata.yaml --css=css/epub.css -o "../_epub/${f%.html}.epub"
done
cd ..

end=$SECONDS
printf "\n\nDuration: $((end-start)) seconds\n"

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class IwataPipeline(object):
    def process_item(self, item, spider):
        return item

import json

class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open("iwata-debug-pipeline.jl", "w")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

import jinja2    # templating
import markdown  # markdown extra
import os        # rename, move, basename
import re        # regex
import hashlib   # sha

TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <title>{{title}}</title>
    <meta charset="UTF-8">
    <link href="css/bootstrap-combined.min.css" rel="stylesheet">
    <link href="css/iwata.css" rel="stylesheet">
</head>
<body>
<div class="container">
{{content}}
</div>
</body>
</html>
"""

class MarkdownWriterPipeline(object):
    all_md = ""
    md = ""
    title = ""

#    def open_spider(self, spider):
#        self.mark = open("iwata.md", "a", encoding="utf-8", errors="xmlcharrefreplace" )
#        self.html = open("iwata.html", "a", encoding="utf-8", errors="xmlcharrefreplace" )

    def close_spider(self, spider):
        self.mark.write( self.all_md )
        self.html.write( jinja2.Template(TEMPLATE).render(content=markdown.markdown(self.all_md, extensions=["extra", "smarty"], output_format="html5"), title=self.title) )
        self.mark.close()
        self.html.close()

    def process_item(self, item, spider):
        self.md = ""

        def replace_all(text, dic):
            for i, j in dic.items():
                text = text.replace(i, j)
            return text

        if "title" in item:
            self.title = item["title"][0] +" - "+ item["title"][2]
            self.mark = open("_md/"+ self.title.replace("Iwata Asks: ", "") +".md", "w", encoding="utf-8", errors="xmlcharrefreplace" )
            self.html = open("_html/"+ self.title.replace("Iwata Asks: ", "") +".html", "w", encoding="utf-8", errors="xmlcharrefreplace" )

        if "heading" in item:
            temp_md = item["heading"][0]
            temp_md = replace_all(temp_md, { "''":"\"", "´": "'" })
            self.md += "### "+ temp_md +"\n\n"

        if "name" in item:
            temp_md = item["text"]
#            temp_md = replace_all(temp_md, { "(laughs)": "😺", "(laugh)":"😹", "(wry laughter)":"😼", "<p>":"", "</p>":""})
#            temp_md = replace_all(temp_md, { "(laughs)": "🙂", "(laugh)":"😂", "(wry laughter)":"😏", "<p>":"", "</p>":""})
            p = re.compile("(\([a-z ]*?\))")
            temp_md = p.sub("_\g<1>_", temp_md)
            self.md += "**"+ item["name"].replace(":", " ") +"**\n: "+ temp_md
                
            if "note_num" in item:
                self.md += " [^"+ item["note_num"] +"]"
            self.md += "\n\n"

        if "image" in item:
            url = "https:"+ item["image"]
            hashed = hashlib.sha1(url.encode())
#            self.md += "!["+ os.path.basename(item["image"]) +"]("+ item["image"] +")\n\n"        # online
            self.md += "![https:"+ item["image"] +"](images/"+ hashed.hexdigest() +".jpg)\n\n"    # local

        self.all_md += self.md

        return item

#!/usr/bin/env python
# -*- coding: utf-8 -*-


import feedparser
from datetime import datetime
from time import mktime
import getapi

#RSSのURL
RSS_URL  = "http://news.yahoo.co.jp/pickup/rss.xml"

#RSSの取得
feed = feedparser.parse(RSS_URL)
allword=''
count=0
feel=0
#RSSのタイトル
print feed.feed.title

for entry in range(len(feed.entries)):
    #RSSの内容を一件づつ処理する
    title = feed.entries[entry].title
    link = feed.entries[entry].link

    #更新日を文字列として取得
    published_string = feed.entries[entry].published

    #更新日をdatetimeとして取得
    tmp = feed.entries[entry].published_parsed
    published_datetime = datetime.fromtimestamp(mktime(tmp))

    #表示
    print title
    print link
    print published_string
    print published_datetime
    allword= allword + title

for words in getapi.split(allword):

    for line in open('pn_ja.dic', 'r'):
        dic=line.split(":")

        if words==unicode(dic[0], 'utf_8'):
            feel = feel + float(dic[3].rstrip())
            count = count + 1
print '================================'
print u'ネガティブ/ポジティブ値'
print feel
print u'平均値'
print feel/count

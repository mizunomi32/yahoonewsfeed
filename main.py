#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser
from urllib import urlopen, quote_plus
from BeautifulSoup import BeautifulSoup
from datetime import datetime
from time import mktime
import yahooapi.jlp as jlp

#RSSのURL
RSS_URL  = "http://news.yahoo.co.jp/pickup/rss.xml"
YAHOO_API = "http://jlp.yahooapis.jp/MAService/V1/parse?appid=dj0zaiZpPWFncG1ZMXUyNU5TRiZzPWNvbnN1bWVyc2VjcmV0Jng9MjM-&sentence="
#RSSの取得
feed = feedparser.parse(RSS_URL)

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

    title.replace(' ', '')
    title.replace(u'　', '')
    #表示
    print title
    print link
    print published_string
    print published_datetime
    getYAHOO_API = YAHOO_API + quote_plus(title.encode('utf-8'))
    feed2 = feedparser.parse(getYAHOO_API)
    print u"~分析結果~"
    print getYAHOO_API

    for entry2 in range(len(feed2.entries)):
        #RSSの内容を一件づつ処理する
        words = feed2.entries[entry2].surface
        read = feed2.entries[entry2].reading
        pos = feed2.entries[entry2].pos

        #表示
        print words
        print read
        print pos

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib import urlopen, quote_plus
from BeautifulSoup import BeautifulSoup


appid='xxxxxxxx'  #APPIDを記述
pageurl='http://jlp.yahooapis.jp/MAService/V1/parse'

#形態素解析した結果をリストで返す
def split(sentence,appid=appid,results='ma',filter='1|2|4|5|9|10',response='surface,reading,pos,baseform'):
    ret=[]
    sentence=quote_plus(sentence.encode('utf-8'))   #urlエンコード
    query="%s?appid=%s&results=%s&response=%s&uniq_filter=%s&sentence=%s" % \
            (pageurl,appid,results,response,filter,sentence)
    soup = BeautifulSoup(urlopen(query))
    try: return [l.baseform.string for l in soup.ma_result.word_list]
    except: return[]

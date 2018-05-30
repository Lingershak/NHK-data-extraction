# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:41:13 2018

@author: bolin.zhao
"""
import urllib2
from urllib2 import urlopen
from bs4 import BeautifulSoup
from urllib2 import HTTPError
try:
        
    html= urlopen("http://www.nhk.or.jp/radionews/")
except urllib2.HTTPError, e:
    print e.code
    print e.read()
else: 
    print html.read()
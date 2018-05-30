# -*- coding: utf-8 -*-
"""
Created on Tue May 29 20:52:44 2018

@author: bolin.zhao
"""
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib import urlretrieve

filePath = '20180530.mp3'
browser = webdriver.Chrome()

browser.get("http://www.nhk.or.jp/radionews/")
html =BeautifulSoup(browser.page_source,"lxml")
#print html
src_audio = str(html.audio['src'])
urlretrieve(src_audio,filePath)

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 23:07:22 2016

@author: Nickhil
"""

from bs4 import BeautifulSoup
import re
import requests

file=input()
with open(file) as f:
    urls = [line.strip() for line in f if line.strip()]
with open('sport1.txt', "r") as word_list:
    list = word_list.read().split('\n')
for url in urls:
    if(url[0]=='w' or url[0]=='h'):
        jhanda=0
        if url[0] != 'h':
            url='http://'+url
        for word in list:
            if word in url :
                print(word)
                jhanda=1
                if jhanda==1:
                    break
        if jhanda==0:
            flag=0
            c=0
            mx=0
            page = requests.get(url).text.lower()
            soup = BeautifulSoup(page,"lxml")
            h=soup.head
            pg=str(h)
            for word in list:
                p = re.compile(word)
                match = re.findall(p,pg)
                if len(match) > 2:
                    c=c+1
                if mx < len(match):
                    mx=len(match)
                    mxwrd=word
            if c>2 or mx==0 or c==0:
                print('NA')
            else:
                print(mxwrd)
            


    
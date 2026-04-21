# -*- coding: utf-8 -*-
import urllib.request
import datetime
import json

client_id = '4I_PCGeCfT46gzmmiHtm'
client_secret = '4Li19IrMMi'

def main():
    
    node = 'news'                                           # 크롤링할 대상
    srcText = input('검색어를 입력하세요: ')
    
    cnt = 0
    jsonResponse = []
    
    jsonResponse = getNaverSearch(node, srcText, 1, 100)    # [CODE 2]
    total = jsonResponse['total']
    
    while ((jsonResponse != None) and (jsonResponse['display'] != 0)):
        for post in jsonResponse['items']:
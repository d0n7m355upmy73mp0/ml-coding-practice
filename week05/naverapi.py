# -*- coding: utf-8 -*-
import urllib.request
import datetime
import json
client_id = 'Client ID'
client_secret = 'Client Secret'

def main():
    nod = 'news'
    srcText = input('검색어를 입력하세요: ')
# -*- coding: utf-8 -*-
# !/python2.7
# Created by Aj nicolas

import requests,crayons
from bs4 import BeautifulSoup

#Change url to whatever site you want to scrape(shopify)
url = ['https://kith.com','https://shop-usa.palaceskateboards.com']

#input or change keywords you want to search for
keywords = [
'yeezy',
'nmd',
'boost',
'sticker',
'yang',
]

headers ={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36'
        '(KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36'}

def findamatch():
    oglen = len(url)
    i = 0
    while i < oglen:

        fixed = url[i] +'/sitemap_products_1.xml'
        print ''
        print crayons.blue(fixed)
        print crayons.blue('--')*38

        r = requests.get(fixed,headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')

        links = []
        for site in soup.findAll('loc'):
            links.append(site.text)
        i += 1

        t = 0
        orig = len(keywords)
        while t < orig:

            matching = [s for s in links if keywords[t] in s]
            print 'FOUND',len(matching), 'LINKS', 'FOR:', keywords[t].upper()
            for item in matching:
                print crayons.green(item)

            t += 1

findamatch()

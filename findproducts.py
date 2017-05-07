# -*- coding: utf-8 -*-
# !/python2.7
# Created by Aj nicolas

import requests,crayons
from bs4 import BeautifulSoup

#Change url site to whatever site you want to scrape
url = 'https://kith.com/'

def linkfriendly():
    global r
    global soup
    
        #Gets user shopify link
    headers ={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36'
            '(KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36'}
    fixed = url +'/sitemap_products_1.xml'
    r = requests.get(fixed ,headers=headers )
    check = r.status_code

    while True:
        if check != 200:
            print crayons.red('Site not found, check link', bold=True)
        else:
            print 'Found:',url
        break
    soup = BeautifulSoup(r.content, 'html.parser')

linkfriendly()


def sites():
	global links
	links = []
	for site in soup.findAll('loc'):
		links.append(site.text)
sites()

#input your keywords you want to search for, input as many as you want!
keywords = [
'yeezy',
'nmd',
'boost',
]

def Findamatch():
	i = 0
	oglen = len(keywords)
	while i < oglen:

		matching = [s for s in links if keywords[i] in s]
		print 'FOUND',len(matching), 'LINKS', 'FOR:', keywords[i].upper()
		for item in matching:
			print crayons.green(item)

		print '--'*38
		i += 1

Findamatch()

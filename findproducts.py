# -*- coding: utf-8 -*-
# !/python2.7
# Created by Aj nicolas

import requests,crayons
from bs4 import BeautifulSoup

#Change url to whatever site you want to scrape(shopify)
url = ['https://www.oneness287.com/','https://cncpts.com/']

#input or change keywords you want to search for
keywords = [
'yeezy',
'nmd',
'boost',
]

headers ={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36'
        '(KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36'}


def findamatch():
    #Goes through every url
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

        #While loop to get all the matching keyword links
        t = 0
        orig = len(keywords)
        while t < orig:

            matching = [s for s in links if keywords[t] in s]
            print 'FOUND',len(matching), 'LINKS', 'FOR:', crayons.blue(keywords[t].upper())

            x = 0
            Mt = len(matching)
            while x < Mt:
                fix = matching[x] + '.xml'
                r = requests.get(fix,headers=headers)
                soup = BeautifulSoup(r.content, 'html.parser')

                #parses for inventory of each link and prints everything out here 
                stk = []
                for stock in soup.findAll("inventory-quantity"):
                    stk.append(int(stock.text))
                print crayons.cyan(matching[x])
                print crayons.green(sum(stk)), 'Total stock'
                print ''

                x += 1

            t += 1
    
findamatch()

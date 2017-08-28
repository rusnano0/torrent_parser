# -*- coding: utf-8 -*-
"""
http://www.torrentino.me/torrents?tags=%D0%BA%D0%BD%D0%B8%D0%B3%D0%B0
http://www.torrentino.me/torrents?page=834&tags=%D0%BA%D0%BD%D0%B8%D0%B3%D0%B0
"""

import requests
from bs4 import BeautifulSoup
from random import choice
import time

from pymongo import MongoClient
client = MongoClient()
db = client.torrent_parser
books = db.books



useragents = open('useragents.txt').read().split('\n')

useragent = {'User-Agent' : choice(useragents)}

def get_html (url, useragent=None, proxies = None):
    """ get the html of pages"""
    r = requests.get(url, headers = useragent, proxies = proxies)
    return r.text

def get_total_pages(html):
    """get total pages"""
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('ul', class_='pagination').find_all('a')[-2].get('href')
    total_pages = pages.split('=')[1].split('&')[0]
    return total_pages

def get_page_data(html):
    """get the page data"""
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find('table', class_='table-list torrents').find_all('tr', class_='item')
    
    for c, item in enumerate(items, 1):
        time.sleep(1)
        try:
            title = item.find('td', class_='name').find('a').get('title')
            size = item.find('td', class_='size').get_text()
            magnet = item.find('td', class_='download').find('a').get('data-default')
            torrent = item.find('td', class_='download').find('a').get('data-not-installed')
            
            url = item.find('td', class_='name').find('a').get('href')
            try:
                description_soup = BeautifulSoup(get_html(url, useragent), 'lxml')
                description =  description_soup.find('div', class_='plate description').get_text()
            except:
                description = ''
#                .sort([('score', {'$meta': 'textScore'})])
            i = {
                    'title' : title,
                    'url' : url,
                    'size' : size,
                    'description' : description,
                    'torrent' : torrent,
                    'magnet' : magnet,
                    }
            books.insert_one(i)
            
            print('{} - inserted with size: {}'.format(c, size))
        except Exception as e:
            print('EXCEPT {} with size: {}\n {}'.format(c, size, e))
            continue

url = 'http://www.torrentino.me/torrents?tags=%D0%BA%D0%BD%D0%B8%D0%B3%D0%B0'
base_url = 'http://www.torrentino.me/torrents?'
page_part = 'page='
query_part = '&tags=%D0%BA%D0%BD%D0%B8%D0%B3%D0%B0'

total_pages = 100 #get_total_pages(get_html(url, useragent))

for i in range(1, int(total_pages)+1):
    url_gen = base_url + page_part + str(i) + query_part
    html = get_html(url_gen, useragent)
    get_page_data(html)
    



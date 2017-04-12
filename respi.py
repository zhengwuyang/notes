'''
4-12
数据还未按条目整理，待更新
'''
from __future__ import print_function
import logging
import requests
import sys
from bs4 import BeautifulSoup
from lxml import html

#设置日志等级为debug,使requests模块命令行调试打印日志，
logging.basicConfig(level=logging.DEBUG)

#headers作为反爬虫的手段，必须添加，有些字段不需添加，以下为必须添加的
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    "Referer": "https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=milk"
}

title = []
price = []
nstar = []


def getamz(keyword, maxpage=None):
    '''
    传入搜索的关键字和最大爬取页数，实现对商品信息的爬取
    '''
    print(keyword,maxpage)
    base_url = 'https://www.amazon.com'
    search_url = base_url + '/s'
    #搜索页面
    params = {
        'url': 'search-alias=aps',
        'field-keywords': keyword
    }
    req = requests.Session()

    response = req.get(search_url, headers=headers, params=params)
    tree = html.fromstring(response.content)

    pname = tree.xpath('//div//a/h2/text()')
    title.extend(pname)

    pstar = tree.xpath('//span/a/i[1]/span/text()')
    for i in pstar:
        i = float(i[:-15])
        nstar.append(i)

    pprice = tree.xpath('//div[4]/div[2]/a/span/@aria-label')
    price.extend(pprice)

    page = tree.xpath('//*[@id="pagn"]/span[6]/text()')
    if maxpage:
        if page:
            page = int(page[0])
            if maxpage < page:
                page = maxpage
            for i in range(page-1):
                next_href = tree.xpath(
                    '//*[@id="pagn"]//a[@title="Next Page"]/@href')

                if next_href:
                    next_url = base_url + next_href[0]
                    response = req.get(next_url, headers=headers)
                    tree = html.fromstring(response.content)

                    pname = tree.xpath('//div//a/h2/text()')
                    title.extend(pname)

                    pstar = tree.xpath('//span/a/i[1]/span/text()')
                    for i in pstar:
                        i = float(i[:-15])
                        nstar.append(i)
                    
                    pprice = tree.xpath('//div[4]/div[2]/a/span/@aria-label')
                    price.extend(pprice)
                else:
                    print('None')
    print(title,nstar,price)
    '''
    with open('html.txt', 'wr') as file:
        file.write(respons.content)
        file.close()
    '''


if __name__ == '__main__':
    getamz(sys.argv[1],int(sys.argv[2]))





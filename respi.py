from __future__ import print_function
import requests
from lxml import html

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Host": "aax-us-east.amazon-adsystem.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    "Referer": "https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=milk"
}


def getamz():
    base_url = 'https://www.amazon.com/'
    req = requests.Session()
    params = {
        'url': 'search-alias=aps',
        'field-keywords': 'milk'
    }

    respons = req.get(base_url, headers=headers)
    print(respons.apparent_encoding)
    print(respons.encoding)

    #text = respons.content.decode(respons.encoding)

    tree = html.fromstring(respons.content)
    print(tree.xpath('//title/text()'))
    pname = tree.xpath('//div//a/h2/text()')
    print(pname)
    '''
    with open('html1.txt', 'wr') as file:
        file.write(respons.content)
    '''


def getjd():
    base_url = 'https://search.jd.com/Search/'
    req = requests.Session()
    params = {
        'keyword': 'milk',
        'enc': 'utf-8',
        'wq': 'milk',
        'pvid': '53b137f96dae4580b0fbcc95eecef086'
    }
    url = 'https://search.jd.com/Search?keyword=milk&enc=utf-8&wq=milk&pvid=cc1f92668c8840d79c2e072421acc81a'

    response = req.get(base_url, params=params)
    print(response.encoding)
    # print(response.content)
    tree = html.fromstring(response.text)
    text = tree.xpath('//title/text()')
    for i in text:
        i.encode('utf-8')
        print(i)
    #pname =  tree.xpath('/*[@id="J_goodsList"]//div//a[@target="_blank"]/em/text()')
    pname = tree.xpath('//*[@id="J_goodsList"]/ul/li[3]/div/div[3]/a/text()')
    for i in pname:
        i.encode('utf-8')
    print(pname)


def test():
    base_url = 'http://econpy.pythonanywhere.com/ex/001.html'
    req = requests.Session()
    respons = req.get(base_url)
    print(respons.encoding)

    text = respons.text.decode(respons.encoding).encode('utf-8')
    tree = html.fromstring(text)

    name = tree.xpath('//div[@title="buyer-name"]/text()')
    # print(name)


if __name__ == '__main__':
    #    test()
    getamz()
    getjd()

from __future__ import print_function
import scrapy
from scrapy.http.cookies import CookieJar
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.http import Request,FormRequest

from mytest.items import myItem

class mySpider(scrapy.Spider):
    name = "myspider"

    allowed_domains = ["www.amazon.com"]

    start_urls =[
        #"https://www.amazon.com/s"
        "https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=milk"
    ]

    headers ={
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Referer": "https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=milk"
    }


    formdata = {
        'url': 'search-alias=aps',
        'field-keywords': 'milk'
    }
    '''
    def start_requests(self):
        return [FormRequest("https://www.amazon.com/s",formdata=self.formdata)]
    '''
    def parse(self, response):
        myitem = myItem()
        items = Selector(response).css('.s-item-container')
        
        for item in items:
            titles = item.css('h2::text').extract_first()
            prices = item.xpath('descendant::div/div/a/span/@aria-label').extract_first()
            #prices = item.css('div>div>a>span').extract_first()
            #prices = item.css('[aria-label]::first_child').extract_first()
            #stars = item.xpath('//span/a/i[1]/span/text()').extract_first()
            stars = item.css('.a-icon-alt::text').extract_first()
            stars = str(stars)[:-15]
            yield myItem(
                title=item.css('h2::text').extract_first(),
                stars=stars,
            )
        #myitem['title'] = p.item.css('h2::text').extract_first()
        print(response.url)
        print(myitem['title'])
        
#atfResults
    '''    
    all_urls = hxs.select('//a/@href').extract()
    for url in all_urls:
        if url.startswith('http://www.xiaohuar.com/list-1-'):
            yield Request(url, callback=self.parse)
            '''
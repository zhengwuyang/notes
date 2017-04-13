from __future__ import print_function
#import scrapy
import re
from scrapy.http.cookies import CookieJar
from scrapy.spiders import Spider, CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.http import Request, FormRequest
from mytest.items import AmazonItem


class AmazonSpider(Spider):

    name = "amazon_search"

    allowed_domains = ["www.amazon.com"]

    base_url = "https://www.amazon.com"

    def __init__(self, *args, **kwargs):
        super(AmazonSpider, self).__init__(*args, **kwargs)

        self.start_urls = [
            "https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords={keywords}".format(keywords=kwargs.get('keyword'))
        ]

        self.maxpage = 20
        if 'maxpage' in kwargs:
            self.maxpage = int(kwargs.get('maxpage'))

        self.page = 0


    def parse(self, response):
        self.page+=1
        if self.page > self.maxpage:
            return
        ama_item = AmazonItem()
        i = 1
        for result in self.parse_results(response):
            print(i)
            i+=1
            title = self.parse_title(result)[0].extract()
            if title is None:
                continue
            ama_item["title"] = title
            ama_item["price"] = self.parse_price(result).extract_first()

            starbuff = str(self.parse_star(result).extract_first())
            ama_item["stars"] = re.findall(r'^\d(?=\s)|^\d.\d', starbuff)

            ama_item ["review"] = self.pare_review(result).extract_first()
            asin_href = str(self.pare_asinhref(result).extract_first())

            ama_item ["asin"] = re.findall(r'(?<=dp/)\S{10}',asin_href)
            
            ama_item["url"] = response.url                    
            yield ama_item
        nexturl_buff = self.pare_nexturl(response).extract_first()
        if nexturl_buff:
            url = response.urljoin(nexturl_buff)
            yield Request(url,headers=self.headers)

    def parse_results(self,response):
        return response.css("ul > .s-item-container")

    def parse_title(self,response):
        return response.css("h2::text")

    def parse_price(self,response):
        return response.css("[aria-label]::attr(aria-label)")

    def parse_star(self,response):
        return response.css(".a-icon-alt::text")

    def pare_review(self,response):
        return response.css(".a-row.a-spacing-top-mini.a-spacing-mini > .a-size-small.a-link-normal.a-text-normal::text")

    def pare_asinhref(self,response):
        return response.css("div.a-fixed-left-grid-col.a-col-right > div.a-row.a-spacing-small > a ::attr(href)")
    def pare_nexturl(self,response):
        return response.css(".pagnNext::attr(href)")


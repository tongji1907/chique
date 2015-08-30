# -*- coding: utf-8 -*-

from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from chique.scrapy.items import ProductLink
from chique.utils.crawlhelper import *
from chique.scrapy.redis_spider import RedisSpider


class JDLinkSpider(RedisSpider):
    name = 'jingdong_link'
    domain = 'http://jdd.jr.jd.com'
    allowed_domains = ['jd.com']
    platform_id = '6'
    platform_code = '100006'
    platform_name = u'京东金融'
    product_line_id = '14'
    start_urls = ['http://jdd.jr.jd.com/product/list/1-6-0-0-0-0-default-1.html']
    cookies = {
        'cookies':{
            ' pinId': 'AtiudGTKS561ffsfn98I-w', 
            ' __jdb': '246537951.2.1549798959|1.1438400182', 
            ' __jdc': '246537951', 
            ' TrackID': '1-FLqUfXvVCdyLggTaFIL1tgeu9Kk4fDeEp0lMMHb6wGosqhHL9jvhcZmdJwyYqHS3KnNGI43uRjNxbKF1uPZQw', 
            ' __jda': '246537951.1549798959.1438258165.1438258165.1438400182.1', 
            ' pin': 'ArvinCao', 
            ' unick': 'ArvinCaomic', 
            '_jrda': '2', 
            ' _pst': 'ArvinCao', 
            ' thor': '4EE21A5559C37F0AEE8115B7396B16E64CBDBECF99349ED8A4423A78ECA66922B5464703EAD7C2D2570D8B05A49498AA6E0E136602EB4746ADF573E93842DD8E67EAD91DB2BFF9BF951D753343EFBEF472203931B9110F97330E91494C326B6B2202FD3F83C188C097EF56796B095A6B35E6817D53E925DFA46B0E842056607AE94CAB39532502E7457C0DB37F8E5F57', 
            ' _tp': 'z42c4TrhQCSTBZLOwfk2HQ%3D%3D', 
            ' __jdv': '246537951|direct|-|none|-', 
            ' __jdu': '1549798959', 
            ' _jrdb': '1438400233731'
            }
        } 
    _table_url = 'http://jdd.jr.jd.com/product/table/%s-10-0-0-0-0-default-1.html'
    _xpath_total_item = '//span[@class="ark-color-red"]/text()'
    _xpath_item_url = '//div[@class="column-first"]/div[1]//a[contains(@href, "detail")]/@href'

    def parse(self, response):
        print 'link:'+response.url
        result = []
        hxs = Selector(response)
        total_item = hxs.xpath(self._xpath_total_item).extract()[0]
        total_page = int(int(total_item) / 10 + 1)
        total_page = 5
        for page in range(1, total_page + 1):
            page_url = self._table_url % str(page)
            r = Request(page_url, cookies=self.cookies, callback=self.parse_list)
            result.append(r)
        print '[total_page]:', total_page
        return result

    def parse_list(self, response):
        result = []
        hxs = Selector(response)
        item_urls = hxs.xpath(self._xpath_item_url).extract()
        for item in item_urls:
            item_url = self.domain + item if self.domain not in item else item
            i = ProductLink()
            i['link_hash'] = convert2md5(item_url)
            i['link_level'] = '1'
            i['product_line_id'] = self.product_line_id
            i['platform_id'] = self.platform_id
            i['url'] = item_url
            i['product_code'] = re.findall(r'[0-9]+', i['url'])[0]
            i['crawl_status'] = '0'
            i['from_url'] = response.url
            i['created_at'] = now()
            i['created_by'] = 'autoload'
            i['updated_at'] = now()
            i['updated_by'] = 'autoload'
            i['spider_id'] = '1'
            i['failed_times'] = '0'
            i['version'] = '0'
            i['cookies'] = str(self.cookies['cookies'])
            i['headers'] = ''
            i['postdata'] = ''
            result.append(i)
            yield i
# -*- coding: utf-8 -*-

from chique.scrapy.redis_spider import RedisSpider
from scrapy.exceptions import CloseSpider


class LinkSpider(RedisSpider):
    name = "link"
    #allowed_domains = ["www.baidu.com"]

    def parse(self, response):
        if self.paused:
            print 'close spider link'
            raise CloseSpider(reason='API usage exceeded')
        #print response.url




    #def make_requests_from_url(self, url):
    #    request = Request(url,cookies = {' pinId': 'AtiudGTKS561ffsfn98I-w', ' __jdb': '246537951.2.1549798959|1.1438400182', ' __jdc': '246537951', ' TrackID': '1-FLqUfXvVCdyLggTaFIL1tgeu9Kk4fDeEp0lMMHb6wGosqhHL9jvhcZmdJwyYqHS3KnNGI43uRjNxbKF1uPZQw', ' __jda': '246537951.1549798959.1438258165.1438258165.1438400182.1', ' pin': 'ArvinCao', ' unick': 'ArvinCaomic', '_jrda': '2', ' _pst': 'ArvinCao', ' thor': '4EE21A5559C37F0AEE8115B7396B16E64CBDBECF99349ED8A4423A78ECA66922B5464703EAD7C2D2570D8B05A49498AA6E0E136602EB4746ADF573E93842DD8E67EAD91DB2BFF9BF951D753343EFBEF472203931B9110F97330E91494C326B6B2202FD3F83C188C097EF56796B095A6B35E6817D53E925DFA46B0E842056607AE94CAB39532502E7457C0DB37F8E5F57', ' _tp': 'z42c4TrhQCSTBZLOwfk2HQ%3D%3D', ' __jdv': '246537951|direct|-|none|-', ' __jdu': '1549798959', ' _jrdb': '1438400233731'},dont_filter=True)
    #    return request
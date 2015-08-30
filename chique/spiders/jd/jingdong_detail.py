# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from chique.scrapy.items import ProductDetail
from chique.scrapy.redis_spider import RedisSpider
from chique.utils.crawlhelper import *


class JDDetailSpider(RedisSpider):

    name = 'jingdong_detail'
    domain = 'http://jdd.jr.jd.com'
    allowed_domains = ['jd.com']
    product_line_id = '14'
    #database = create_mysql_connection()
    
    # 产品名称
    _xpath_product_name = '//div[@id="bond-profile"]//span[@class="ark-panel-title"]//strong/text()'
    # 投资总额
    _xpath_investment_amount = '//div[@id="secondaryProfile"]//div[@class="ark-table-body"]/div[1]//span[@class="ark-margin-left-10 f14"]/text()'
    # 最小投资金额
    _xpath_investment_amount_min = '//div[@id="bond-investment"]//div[@class="row h40"]//strong[@class="ark-color-orange"]/text()'
    # 最大投资金额
    _xpath_investment_amount_max = '//div[@id="bond-investment"]//div[@class="row"]//strong[@class="ark-color-orange"]/text()'
    # 投资周期
    _xpath_investment_period = '//div[@class="row h100"]/div[4]//span[@class="value"]/text()'
    # 最小年化收益
    _xpath_annualized_return_rate_min = '//div[@class="row h100"]/div[2]//span[@class="value"]/text()'
    # 最大年化收益
    _xpath_annualized_return_rate_max = '//div[@class="row h100"]/div[2]//span[@class="value"]/text()'
    # 安全保障
    _xpath_safeguard_mode = '//div[@class="row h100"]/div[6]//span[@class="ark-bg-badge-blank"]/text()'
    # 安全保障信息
    _xpath_safeguard_mode_text = '//div[@class="row h100"]/div[6]//span[@class="ark-bg-badge-blank"]/text()'
    # 发布周期
    _xpath_publish_period = '//none'
    # 起始日期
    _xpath_start_date = '//div[@id="secondaryProfile"]//div[@class="ark-table-body"]/div[1]/div[3]//span[@class="ark-margin-left-10"]/text()'
    # 结束日期
    _xpath_end_date = '//none'
    # 投资人数
    _xpath_num = '//div[@class="subtitle"]//strong[@class="ark-color-black"]/text()'
    # 进度
    _xpath_progress = '//div[@class="progress ark-progressbar w300 h10 ark-margin-top-6"]/div[1]/@data-value'
    # 剩余金额
    _xpath_remain_amount = '//div[@class="row h30 ark-margin-top-20"]//span[@class="ark-margin-left-10"]//text()'

    '''
    def start_requests(self,):
        item_urls = get_link_new(self.database, self.product_line_id)
        result = [Request(item['url'], cookies=eval(item['cookies']), callback=self.parse_detail, 
        meta={'product_code':item['product_code'], 'link_hash': item['link_hash']}) for item in item_urls[:10]]
        return result
    '''
    def parse(self, response):
        print "details:" +response.url

        hxs = Selector(response)
        i = ProductDetail()
        i['link_hash'] = response.meta['link_hash']
        i['product_url'] = response.url
        i['product_name'] = get_content(hxs.xpath(self._xpath_product_name).extract())
        i['product_code'] = response.meta['product_code']
        i['product_description'] = ''
        amount = get_content(hxs.xpath(self._xpath_investment_amount).extract())
        i['investment_amount'] = get_money(amount)
        amount_min = get_content(hxs.xpath(self._xpath_investment_amount_min).extract())
        i['investment_amount_min'] = get_money(amount_min)
        amount_max = get_content(hxs.xpath(self._xpath_investment_amount_max).extract())
        i['investment_amount_max'] = get_money(amount_max)
        i['investment_period'] = get_content(hxs.xpath(self._xpath_investment_period).extract())
        i['annualized_return_rate_min'] = get_content(hxs.xpath(self._xpath_annualized_return_rate_min).extract())
        i['annualized_return_rate_max'] = get_content(hxs.xpath(self._xpath_annualized_return_rate_max).extract())
        i['safeguard_mode'] = 0
        i['safeguard_mode_text'] = get_content(hxs.xpath(self._xpath_safeguard_mode_text).extract())
        i['publish_period'] = get_content(hxs.xpath(self._xpath_publish_period).extract())
        i['start_date'] = get_content(hxs.xpath(self._xpath_start_date).extract())
        i['end_date'] = get_content(hxs.xpath(self._xpath_end_date).extract())
        remain_amount = get_content(hxs.xpath(self._xpath_remain_amount).extract())
        i['remain_amount'] = get_money(remain_amount)
        i['remain_time'] = ''
        i['progress'] = get_content(hxs.xpath(self._xpath_progress).extract())
        i['promotion'] = ''
        i['created_at'] = now()
        i['created_by'] = 'autoload'
        i['updated_at'] = now()
        i['updated_by'] = 'autoload'
        i['failed_times'] = 0
        i['invest_num'] = get_content(hxs.xpath(self._xpath_num).extract())
        i['product_status'] = '0'
        i['version'] = 0
        yield i

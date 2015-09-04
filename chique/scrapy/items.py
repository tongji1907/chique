# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ProductLink(scrapy.Item):
    # link base data structure
    link_hash = scrapy.Field()
    link_level = scrapy.Field()
    product_line_id = scrapy.Field()
    platform_id = scrapy.Field()
    url = scrapy.Field()
    product_code = scrapy.Field()
    crawl_status = scrapy.Field()
    from_url = scrapy.Field()
    created_at = scrapy.Field()
    created_by = scrapy.Field()
    updated_at = scrapy.Field()
    updated_by = scrapy.Field()
    spider_id = scrapy.Field()
    failed_times = scrapy.Field()
    version = scrapy.Field()
    cookies = scrapy.Field()
    headers = scrapy.Field()
    postdata = scrapy.Field()



class ProductDetail(scrapy.Item):
    # product detail data structure
    link_hash = scrapy.Field()
    product_url = scrapy.Field()
    product_name = scrapy.Field()
    product_code = scrapy.Field()
    product_description = scrapy.Field()
    investment_amount = scrapy.Field()
    investment_amount_min = scrapy.Field()
    investment_amount_max = scrapy.Field()
    investment_period = scrapy.Field()
    annualized_return_rate_min = scrapy.Field()
    annualized_return_rate_max = scrapy.Field()
    safeguard_mode = scrapy.Field()
    safeguard_mode_text = scrapy.Field()
    publish_period = scrapy.Field()
    start_date = scrapy.Field()
    end_date = scrapy.Field()
    remain_amount = scrapy.Field()
    remain_time = scrapy.Field()
    progress = scrapy.Field()
    promotion = scrapy.Field()
    created_at = scrapy.Field()
    created_by = scrapy.Field()
    updated_at = scrapy.Field()
    updated_by = scrapy.Field()
    #failed_times = scrapy.Field()
    invest_num = scrapy.Field()
    product_status = scrapy.Field()
    #version = scrapy.Field()

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from chique.utils.crawlhelper import *


class MySQLPipeline(object):

    def __init__(self):
        self.database = create_mysql_connection()

    def process_item(self, item, spider):
        if 'link' in spider.name:
            into_link_new(self.database, dict(item))
            return item
        elif 'detail' in spider.name:
            into_detail(self.database, dict(item))
            return item

#!/usr/bin/env python
__author__ = 'wuyan'
from chique.spiders.jd.jingdong_detail import JDDetailSpider
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from scrapy.spiderloader import SpiderLoader
settings = Settings()
settings_module_path = "settings"
if settings_module_path:

    settings.setmodule(settings_module_path, priority='project')

process = CrawlerProcess(settings)

process.crawl()


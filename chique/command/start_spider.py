#!/usr/bin/env python
from scrapy.crawler import CrawlerProcess
from threading import Thread
from scrapy.settings import Settings
from scrapy.spiderloader import SpiderLoader
import time

settings = Settings()
settings_module_path = "settings"
if settings_module_path:
    settings.setmodule(settings_module_path, priority='project')
process = CrawlerProcess(settings)

def _start_crawler_thread():
    t = Thread(target=process.start,kwargs={'stop_after_crawl': False})
    t.daemon = True
    t.start()


loader = SpiderLoader(settings)

for spider_cls in loader._spiders:

    process.crawl(spider_cls)

_start_crawler_thread()

while 1:
    time.sleep(2)


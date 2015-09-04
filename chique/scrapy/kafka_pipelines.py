__author__ = 'wuyan'
from kafka.client import KafkaClient
from kafka.producer import SimpleProducer
from kafka.consumer import SimpleConsumer

class KafkaPipeline(object):

    def __init__(self):
        self.client  = KafkaClient("120.25.216.93:9092")

    def process_item(self, item, spider):
        if 'link' in spider.name:

            return item
        elif 'detail' in spider.name:

            return item
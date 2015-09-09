__author__ = 'wuyan'
from kafka.client import KafkaClient
from kafka.producer import SimpleProducer
from kafka.consumer import SimpleConsumer
from avro_json_serializer import *
from chique.scrapy.avro.schema import *
from chique.utils.connection_factory import ConnectionFactory
import json
import jsonpickle

class KafkaPipeline(object):

    def __init__(self):
        self.client  = ConnectionFactory().create_kafka_connection(self.settings)

    @classmethod
    def from_settings(cls, settings):
        cls.settings = settings
        return cls()

    def process_item(self, item, spider):
        if 'link' in spider.name:
            link_avro_schema = avro.schema.make_avsc_object(link_schema_dict, avro.schema.Names())
            serializer = AvroJsonSerializer(link_avro_schema)
            d=item.__dict__
            d=d["_values"]
            #print(d)
            json_str = serializer.to_json(d)
            #print json_str
            #json_str = jsonpickle.encode(item,unpicklable=False,make_refs=False)
            #print json_str
            return item
        elif 'detail' in spider.name:

            return item
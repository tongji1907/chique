__author__ = 'william.wu'
from kafka.client import KafkaClient
from kafka.producer import SimpleProducer
from kafka.consumer import SimpleConsumer
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')

kafka = KafkaClient("120.25.216.93:9092")

producer = SimpleProducer(kafka,async=False)
try:
    producer.send_messages("commands", "link_start")
except:
    None
    #time.sleep(1)
    #producer.send_messages("commands", "link1_start")



#consumer = SimpleConsumer(kafka,"commands","F")

#print len(consumer.get_messages())
#for msg in consumer.get_messages():
#    print msg



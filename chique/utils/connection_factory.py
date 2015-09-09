__author__ = 'wuyan'
import redis
from kafka.client import KafkaClient
import MySQLdb

# Default values.

REDIS_HOST = 'localhost'
REDIS_PORT = 6379

KAFKA_HOST = 'localhost'
KAFKA_PORT = 9092



class ConnectionFactory:

    def create_redis_connection(self,settings):

        host = settings.get('REDIS_HOST', REDIS_HOST)
        if host is None:
            host = REDIS_HOST
        port = settings.get('REDIS_PORT', REDIS_PORT)
        if port is None:
            port = REDIS_PORT

        return redis.Redis(host=host, port=port)

    def create_kafka_connection(self,settings):

        host = settings.get('KAFKA_HOST', KAFKA_HOST)
        if host is None:
            host = KAFKA_HOST

        port = settings.get('KAFKA_PORT', KAFKA_PORT)
        if port is None:
            port = KAFKA_PORT

        return KafkaClient(host+":"+ str(port))

    def create_mysql_connection(self,settings):

        host = settings.get('REDIS_HOST', REDIS_HOST)
        port = settings.get('REDIS_PORT', REDIS_PORT)


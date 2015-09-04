__author__ = 'wuyan'
# default
from sqlalchemy import *
from sqlalchemy.sql import select
import pickle
import redis

PWD='admin@00%'
USR='admin'
HOST='120.25.216.93'
DB = 'crawldb'
SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}:3306/{}'.format(USR,PWD,HOST,DB)

print SQLALCHEMY_DATABASE_URI

server =  redis.Redis('120.25.216.93','6379')
engine = create_engine(SQLALCHEMY_DATABASE_URI)

meta = MetaData()
linkbase = Table('linkbase', meta, autoload=True, autoload_with=engine)
s = select([linkbase]).where(linkbase.c.crawl_status<1)
result = engine.execute(s)

for url in result:
    m = pickle.dumps(url)
    print url['spider_id']
    server.lpush(url['spider_id']+":start_urls",m)



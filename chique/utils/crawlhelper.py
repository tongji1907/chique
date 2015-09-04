# -*- coding: utf-8 -*-
# Author: Arvin


import requests
from scrapy.selector import HtmlXPathSelector
import MySQLdb
# from decimal import *
# import datetime
import time
import re
import ConfigParser
import hashlib

import MySQLdb.cursors



DB_HOST = '120.25.216.93'
DB_USER = 'admin'
DB_PASSWD = 'admin@00%'
DB_NAME = 'crawldb'
DB_CHARSET = 'utf8'

def convert2md5(string):
    m = hashlib.md5()
    m.update(string)
    return m.hexdigest()


def create_mysql_connection():
    connection = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWD,
                                 db=DB_NAME, charset=DB_CHARSET, cursorclass=MySQLdb.cursors.DictCursor)
    return connection


def mysql_connect():
    # 建立数据库连接
    config = ConfigParser.ConfigParser()
    config.read('setting.conf')
    mysql = config.items('mysql')
    mysql_config = dict()
    for item in mysql:
        mysql_config[item[0]] = item[1]
    connection = MySQLdb.connect(host=mysql_config['host'], user=mysql_config['user'], passwd=mysql_config['passwd'],
                                 db=mysql_config['db'], charset=mysql_config['charset'])
    return connection


def mysql_connect_new():
    # 建立数据库连接
    config = ConfigParser.ConfigParser()
    config.read('setting.conf')
    mysql = config.items('mysql')
    mysql_config = dict()
    for item in mysql:
        mysql_config[item[0]] = item[1]
    connection = MySQLdb.connect(host=mysql_config['host'], user=mysql_config['user'], passwd=mysql_config['passwd'],
                                 db='crawldb', charset=mysql_config['charset'])
    return connection


def execute_sql(database, sql):
    # 执行sql语句
    cursor = database.cursor()
    cursor.execute(sql)
    database.commit()
    cursor.close()


def into_link(database, dict_data):
    # 存储url
    try:
        keys = ['product_line_id', 'url', 'progress', 'created_at', 'created_by', 'updated_at',
                'updated_by', 'meta_data']
        sql = 'insert into link(' + ','.join(keys) + ') values(' + ','.join(['"%s"'] * len(keys)) + ');'
        sql_string = sql % tuple([dict_data[item] for item in keys])
        print '[into_link_sql]:', sql_string
        execute_sql(database, sql_string)
    except Exception, e:
        print '[into_link_err]:', e


def into_link_new(database, dict_data):
    # 存储url
    try:
        keys = ['link_hash', 'link_level', 'product_line_id', 'platform_id', 'url', 'product_code','from_url', 'created_at', 'created_by', 'updated_at', 'updated_by', 'spider_id', 'cookies', 'headers', 'postdata']
        sql = 'insert into linkbase(' + ','.join(keys) + ') values(' + ','.join(['"%s"'] * len(keys)) + ');'
        sql_string = sql % tuple([dict_data[item] for item in keys])
        print '[into_link_sql]:', sql_string
        execute_sql(database, sql_string)
    except Exception, e:
        print '[into_link_err]:', e


def into_detail(database, dict_data):
    # 存储detail
    try:
        keys = ['link_hash', 'product_url', 'product_name', 'product_code', 'product_description', 'investment_amount','investment_amount_min', 'investment_amount_max', 'investment_period', 'annualized_return_rate_min','annualized_return_rate_max', 'safeguard_mode', 'safeguard_mode_text', 'publish_period', 'start_date','end_date', 'remain_amount', 'remain_time', 'progress', 'promotion', 'created_at', 'created_by', 'updated_at', 'updated_by','invest_num', 'product_status']
        sql = 'insert into detailbaseflow(' + ','.join(keys) + ') values(' + ','.join(['"%s"'] * len(keys)) + ');'
        sql_string = sql % tuple([dict_data[item] for item in keys])
        print '[into_detail_sql]:', sql_string
        execute_sql(database, sql_string)
    except Exception, e:
        print '[into_detail_err]:', e


def get_mysql_structure(database, table_name):
    # 获取MySQL中的表结构
    sql = 'show fields from %s;' % table_name
    cursor = database.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    result = [item[0] for item in res]
    return result


def pagesource(url, mate_data, access_type):
    # 获取网页源文件
    r = None
    if 'data' not in mate_data:
        mate_data['data'] = ''
    if 'cookies' not in mate_data:
        mate_data['cookies'] = ''
    if 'headers' not in mate_data:
        mate_data['headers'] = ''
    if access_type == 'get':
        r = requests.get(url, data=mate_data['data'], cookies=mate_data['cookies'], headers=mate_data['headers'])
    elif access_type == 'post':
        r = requests.post(url, data=mate_data['data'], cookies=mate_data['cookies'], headers=mate_data['headers'], verify=False)
    return r.content


def pagesource2hxs(html_pagesource):
    # 网页源文件转化为xpath对象
    return HtmlXPathSelector(text=html_pagesource)


def get_content(table):
    # 获取xpath中内容
    result = ''
    for item in table:
        result += item.strip()
    return result


def now():
    # 当前时间
    return time.strftime('%Y-%m-%d %X', time.localtime())


def parse_cookies(cookies_string):
    # 处理cookies
    result = dict()
    table = cookies_string.split(';')
    table = [item.split('=') for item in table]
    for item in table:
        result[str(item[0])] = str(item[1])
    return result


def get_data(database, sql_string):
    # 读取数据库数据
    cursor = database.cursor()
    cursor.execute(sql_string)
    data = cursor.fetchall()
    cursor.close()
    # return [list(item) for item in data]
    return data


def get_link(database, product_line_id):
    # 读出对应产品的url
    sql = 'select * from link where progress = "0" and product_line_id = %s;'
    sql_string = sql % str(product_line_id)
    result = get_data(database, sql_string)
    return result


def get_link_new(database, product_line_id):
    # 读出对应产品的url
    sql = 'select * from linkbase where crawl_status = "0" and product_line_id = %s;'
    sql_string = sql % str(product_line_id)
    result = get_data(database, sql_string)
    return result


def update_link_progress(database, link_id):
    # 更新link采集过程
    sql = 'update link set progress = "%s", updated_at = "%s" where link_id = %s;'
    sql_string = sql % (str(1), now(), str(link_id))
    execute_sql(database, sql_string)


def get_number(string):
    result = re.findall(r'[0-9.]+', string)
    return result[0]


def parse_config(config_name):
    config = ConfigParser.ConfigParser()
    config.read('setting.conf')
    config = config.items(config_name)
    result = dict()
    for item in config:
        result[str(item[0])] = str(item[1])
    return result


def random_string():
    # 生成随机数
    return str(int(time.time() * 1000))
    

def get_money(string):
    temp = re.findall(r'[,.0-9]+', string)
    if temp == []:
        return ''
    else:
        temp = temp[0].replace(',','')
        if u'万' in string:
            result = float(temp) * 10000
        else:
            result = float(temp)
        return str(result)
# -*- coding: utf-8 -*-
from avro_json_serializer import *
from chique.scrapy.avro.schema import *

link_avro_schema = avro.schema.make_avsc_object(link_schema_dict, avro.schema.Names())
serializer = AvroJsonSerializer(link_avro_schema)

obj={'result': {'cookies': "{' TrackID': '1-FLqUfXvVCdyLggTaFIL1tgeu9Kk4fDeEp0lMMHb6wGosqhHL9jvhcZmdJwyYqHS3KnNGI43uRjNxbKF1uPZQw', '_jrda': '2', ' _pst': 'ArvinCao', ' thor': '4EE21A5559C37F0AEE8115B7396B16E64CBDBECF99349ED8A4423A78ECA66922B5464703EAD7C2D2570D8B05A49498AA6E0E136602EB4746ADF573E93842DD8E67EAD91DB2BFF9BF951D753343EFBEF472203931B9110F97330E91494C326B6B2202FD3F83C188C097EF56796B095A6B35E6817D53E925DFA46B0E842056607AE94CAB39532502E7457C0DB37F8E5F57', ' pinId': 'AtiudGTKS561ffsfn98I-w', ' pin': 'ArvinCao', ' __jdb': '246537951.2.1549798959|1.1438400182', ' __jdc': '246537951', ' __jda': '246537951.1549798959.1438258165.1438258165.1438400182.1', ' unick': 'ArvinCaomic', ' _jrdb': '1438400233731', ' _tp': 'z42c4TrhQCSTBZLOwfk2HQ%3D%3D', ' __jdv': '246537951|direct|-|none|-', ' __jdu': '1549798959'}",
 'created_at': '2015-09-05 00:03:10',
 'created_by': 'autoload',
 'from_url': 'http://jdd.jr.jd.com/product/table/4-10-0-0-0-0-default-1.html',
 'headers': '',
 'link_hash': 'ef206c401acfe9a0f939d7386a1ea913',
 'link_level': '1',
 'platform_id': '6',
 'postdata': '',
 'product_code': u'5236',
 'product_line_id': '14',
 'spider_id': 'jingdong_detail',
 'updated_at': '2015-09-05 00:03:10',
 'updated_by': 'autoload',
 'url': u'http://jdd.jr.jd.com/detail/bond/5236.html'},
 'status': 'success',
 'timestamp': '2015-09-05 00:03:10',
 'url': 'http://jdd.jr.jd.com/product/table/4-10-0-0-0-0-default-1.html'}

obj1={"url":"http://baidu.com","status": "success", "timestamp":"2015-09-05 20:30:25","result":

    {
     "link_hash":"07f55b2a940e5c0ecdfe204fbbb3f887",
     "link_level":"1",
     "product_line_id":"13",
     "platform_id":"6",
     "url":"http://jdd.jr.jd.com/detail/bond/3818.html",
     "product_code":"3818",
     "from_url":"http://jdd.jr.jd.com/product/table/24-10-0-0-0-0-default-1.html",
     "created_at":"2015-08-13 19:00:45",
     "created_by":"auto",
     "updated_at":"2015-08-13 19:00:45",
     "updated_by":"auto",
     "spider_id":"jingdong_detail",
     "cookies":"",
     "headers":"",
     "postdata":""
    }
}

json =serializer.to_json(obj)

print "link json :" + json

json = serializer.to_json(obj1)

print "link json :" + json

'''
detail_avro_schema = avro.schema.make_avsc_object(detail_schema_dict, avro.schema.Names())
serializer = AvroJsonSerializer(detail_avro_schema)
json = serializer.to_json({"status": "success", "url":"http://baidu.com","timestamp":"2015-09-05 20:30:25","result":

    {"link_hash":"07f55b2a940e5c0ecdfe204fbbb3f887",
     "product_url":"http://jdd.jr.jd.com/detail/bond/4822.html",
     "product_name":"金点点-稳稳赚CQFAE007043",
     "product_code":"4822",
     "product_description":"",
     "investment_amount":"2000000.0",
     "investment_amount_min":"10000.0",
     "investment_amount_max":"50000.0",
     "investment_period":"731",
     "annualized_return_rate_min":"8.50",
     "annualized_return_rate_max":"8.50",
     "safeguard_mode":"",
     "safeguard_mode_text":"金融机构或担保公司本息保障",
     "start_date":"2015-08-30",
     "end_date":"",
     "remain_time":"",
     "remain_amount":"2000000.0000",
     "progress":"0",
     "promotion":"",
     "invest_num":"",
     "product_status":"",
     "created_at":"2015-08-13 19:00:45",
     "created_by":"auto",
     "updated_at":"2015-08-13 19:00:45",
     "updated_by":"auto"
    }
})

print "detail json: " + json
'''
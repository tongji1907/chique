from avro_json_serializer import *
from chique.scrapy.avro.schema import *

link_avro_schema = avro.schema.make_avsc_object(link_schema_dict, avro.schema.Names())
serializer = AvroJsonSerializer(link_avro_schema)
json = serializer.to_json({"status": "success", "url":"http://baidu.com","timestamp":"2015-09-05 20:30:25","result":

    {"link_hash":"07f55b2a940e5c0ecdfe204fbbb3f887",
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
})

print "link json :" + json


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
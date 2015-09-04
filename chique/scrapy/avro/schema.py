__author__ = 'wuyan'

link_schema_dict = { "namespace": "chique.avro",
          "type": "record",
          "name": "LinkResult",
          "fields": [
              {"name": "status", "type": "string"},
              {"name": "url", "type": "string"},
              {"name": "timestamp",  "type": "string"},
              {"name": "result",
                    "type": {
                        "type" : "record",
                        "name" : "LinkItem",
                        "fields" : [
                            {"name": "link_hash", "type": "string"},
                            {"name": "link_level", "type": "string"},
                            {"name": "product_line_id", "type": "string"},
                            {"name": "platform_id", "type": "string"},
                            {"name": "url", "type": "string"},
                            {"name": "product_code", "type": "string"},
                            {"name": "from_url", "type": "string"},
                            {"name": "created_at", "type": "string"},
                            {"name": "created_by", "type": "string"},
                            {"name": "updated_at", "type": "string"},
                            {"name": "updated_by", "type": "string"},
                            {"name": "spider_id", "type": "string"},
                            {"name": "cookies", "type": "string"},
                            {"name": "headers", "type": "string"},
                            {"name": "postdata", "type": "string"}
                        ]
                    }
              }
          ]
}


detail_schema_dict = {"namespace": "chique.avro",
          "type": "record",
          "name": "DetailResult",
          "fields": [
              {"name": "status", "type": "string"},
              {"name": "url", "type": "string"},
              {"name": "timestamp",  "type": "string"},
              {"name": "result",
                    "type": {
                        "type" : "record",
                        "name" : "DetailItem",
                        "fields" : [
                            {"name": "link_hash", "type": "string"},
                            {"name": "product_url", "type": "string"},
                            {"name": "product_name", "type": "string"},
                            {"name": "product_code", "type": "string"},
                            {"name": "product_description", "type": "string"},
                            {"name": "investment_amount", "type": "string"},
                            {"name": "investment_amount_min", "type": "string"},
                            {"name": "investment_amount_max", "type": "string"},
                            {"name": "investment_period", "type": "string"},
                            {"name": "annualized_return_rate_min", "type": "string"},
                            {"name": "annualized_return_rate_max", "type": "string"},
                            {"name": "safeguard_mode", "type": "string"},
                            {"name": "safeguard_mode_text", "type": "string"},
                            {"name": "start_date", "type": "string"},
                            {"name": "end_date", "type": "string"},
                            {"name": "remain_time", "type": "string"},
                            {"name": "remain_amount", "type": "string"},
                            {"name": "progress", "type": "string"},
                            {"name": "promotion", "type": "string"},
                            {"name": "invest_num", "type": "string"},
                            {"name": "product_status", "type": "string"},
                            {"name": "created_at", "type": "string"},
                            {"name": "created_by", "type": "string"},
                            {"name": "updated_at", "type": "string"},
                            {"name": "updated_by", "type": "string"}
                        ]
                    }
              }
          ]
}






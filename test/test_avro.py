__author__ = 'wuyan'
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter


schema_dict = {
    "namespace": "example.avro",
          "type": "record",
          "name": "User",
          "fields": [
              {"name": "name", "type": "string"},
              {"name": "favorite_number",  "type": ["int", "null"]},
              {"name": "favorite_color", "type": ["string", "null"]}
          ]
}
schema = avro.schema.make_avsc_object(schema_dict, avro.schema.Names())
#schema = avro.schema.parse(open("users.avsc").read())

writer = DataFileWriter(open("users.avro", "w"), DatumWriter(), schema)
writer.append({"name": "Alyssa", "favorite_number": 256})
writer.append({"name": "Ben", "favorite_number": 7, "favorite_color": "red"})
writer.close()

reader = DataFileReader(open("users.avro", "r"), DatumReader())
for user in reader:
    print user
reader.close()
from kafka import KafkaProducer
import json

producer = KafkaProducer(retries=5, bootstrap_servers=['localhost:9092'])

def on_success(record):
  print(record.topic)
  print(record.partition)
  print(record.offset)

def on_error(excp):
  print(excp)
  raise Exception(excp)

producer.send('miso', json.dumps({'key': 'value'}).encode('utf-8')).add_callback(on_success).add_errback(on_error)
producer.flush()
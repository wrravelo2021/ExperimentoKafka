from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('miso',
  group_id='my-group', enable_auto_commit=False,
  bootstrap_servers=['localhost:9092'],
  value_deserializer=lambda m: json.loads(m.decode('ascii'))
)

for message in consumer:
  print(message.value)
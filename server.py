from flask import Flask, jsonify
import json
from kafka import KafkaProducer

app = Flask(__name__)

@app.route('/process')
def index():
  send_message()
  return jsonify({"mssg": "Started to process"})

def send_message():
  producer = KafkaProducer(retries=5, bootstrap_servers=['localhost:9092'])
  producer.send('miso', json.dumps({'key': 'value'}).encode('utf-8'))
  producer.flush()
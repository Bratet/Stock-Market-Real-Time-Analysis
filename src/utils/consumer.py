from kafka import KafkaConsumer
import json

class SparkJobConsumer:
    def __init__(self, topic_name, bootstrap_servers='localhost:9092', group_id=None):
        self.consumer = KafkaConsumer(
            topic_name,
            bootstrap_servers=bootstrap_servers,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id=group_id,
            value_deserializer=lambda x: json.loads(x.decode('utf-8')))

    def consume_stock_data(self):
        for message in self.consumer:
            print(f"Received message: {message.value}")
    
    def start(self):
        self.consume_stock_data()

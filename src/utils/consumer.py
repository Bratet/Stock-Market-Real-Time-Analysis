from kafka import KafkaConsumer
import json


class StockConsumer:
    def __init__(self, topic_name, bootstrap_servers='localhost:9092'):
        self.consumer = KafkaConsumer(
            topic_name,
            bootstrap_servers=bootstrap_servers,
            auto_offset_reset='latest',
            enable_auto_commit=False,
            group_id='consumer-group',
            value_deserializer=lambda x: json.loads(x.decode('utf-8')))

    def consume_stock_data(self):
        try:
            for message in self.consumer:
                print(f"Received message: {message.value}")

                self.consumer.commit()
        except Exception as e:
            print(f"Error: {str(e)}")

    def start(self):
        self.consume_stock_data()

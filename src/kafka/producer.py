import time
import json
from kafka import KafkaProducer
from ..utils import fetch_stock_data


def main():
    producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    while True:
        data = fetch_stock_data("AAPL")
        producer.send('stock-data', value=data)
        time.sleep(300)

if __name__ == "__main__":
    main()

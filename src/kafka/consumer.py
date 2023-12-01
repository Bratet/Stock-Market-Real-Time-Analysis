from kafka import KafkaConsumer
import json

def main():
    consumer = KafkaConsumer(
        'stock-data',
        bootstrap_servers=['kafka:9092'],
        auto_offset_reset='earliest',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    for message in consumer:
        message_value = message.value
        print(f"Received stock data: {message_value}")

if __name__ == "__main__":
    main()

from utils.consumer import StockConsumer
from utils.producer import StockProducer
import threading


def main():

    print("Main Application Started")

    topic_name = 'stock_data'

    company = 'TSLA'

    # Initialize Kafka producer and consumer
    producer = StockProducer(
        company, topic_name, bootstrap_servers='localhost:9092')
    consumer = StockConsumer(topic_name)

    # Start producer and consumer in separate threads
    producer_thread = threading.Thread(target=producer.start)

    consumer_thread = threading.Thread(target=consumer.start)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()


if __name__ == "__main__":
    main()

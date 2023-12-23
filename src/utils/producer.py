import yfinance as yf
from kafka import KafkaProducer
import json
import time

class StockProducer:
    def __init__(self, company, topic_name, bootstrap_servers='localhost:9092'):
        self.company = company
        self.topic_name = topic_name
        self.producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                                      value_serializer=lambda x: json.dumps(x).encode('utf-8'))

    def fetch_stock_data(self, stock_symbol):
        stock = yf.Ticker(stock_symbol)
        data = stock.history(period="max", interval="1m")
        return data.tail(1).to_dict(orient="records")[0]

    def produce_stock_data(self, stock_symbol):
        while True:
            print(f"Fetching data for {stock_symbol}")
            data = self.fetch_stock_data(stock_symbol)
            self.producer.send(self.topic_name, value=data)
            time.sleep(10)

    def start(self):
        self.produce_stock_data(self.company)

class TweetProducer:
    def __init__(self, topic_name, bootstrap_servers='localhost:9092'):
        self.topic_name = topic_name
        self.producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                                      value_serializer=lambda x: json.dumps(x).encode('utf-8'))

    def produce_tweets(self):
        while True:
            print("Fetching tweets")
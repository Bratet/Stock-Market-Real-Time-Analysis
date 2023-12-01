from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

def main():
    spark = SparkSession.builder.appName("StockDataAnalysis").getOrCreate()

    schema = StructType([
        StructField("Open", DoubleType()),
        StructField("High", DoubleType()),
        StructField("Low", DoubleType()),
        StructField("Close", DoubleType()),
        StructField("Volume", DoubleType()),
    ])

    df = spark.readStream.format("kafka")\
        .option("kafka.bootstrap.servers", "kafka:9092")\
        .option("subscribe", "stock-data")\
        .load()

    stock_data = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

    query = stock_data.writeStream.outputMode("append").format("console").start()
    query.awaitTermination()

if __name__ == "__main__":
    main()

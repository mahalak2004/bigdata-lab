from pyspark.sql import SparkSession
from pyspark.sql.functions import avg
from pyspark.sql.window import Window

spark = SparkSession.builder \
    .appName("Stock Market Moving Average") \
    .master("local[*]") \
    .getOrCreate()

data = [
    ("2026-01-01", 100.0),
    ("2026-01-02", 105.0),
    ("2026-01-03", 110.0),
    ("2026-01-04", 108.0),
    ("2026-01-05", 115.0)
]

df = spark.createDataFrame(data, ["Date", "ClosingPrice"])

df = df.orderBy("Date")

window = Window.orderBy("Date").rowsBetween(-2, 0)

result = df.withColumn(
    "MovingAverage",
    avg("ClosingPrice").over(window)
)

result.show()

spark.stop()

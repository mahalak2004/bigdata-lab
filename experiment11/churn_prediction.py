
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator

spark = SparkSession.builder \
    .appName("Customer Churn Prediction") \
    .master("local[*]") \
    .getOrCreate()

# Sample customer data:
# UsageHours, SupportCalls, Churn
data = [
    (2.0, 5.0, 1.0),
    (3.0, 4.0, 1.0),
    (4.0, 3.0, 1.0),
    (5.0, 2.0, 0.0),
    (6.0, 1.0, 0.0),
    (7.0, 1.0, 0.0),
    (2.5, 6.0, 1.0),
    (6.5, 2.0, 0.0),
    (3.5, 5.0, 1.0),
    (5.5, 1.0, 0.0),
    (4.5, 4.0, 1.0),
    (7.5, 0.0, 0.0)
]

df = spark.createDataFrame(
    data, ["UsageHours", "SupportCalls", "label"]
)

assembler = VectorAssembler(
    inputCols=["UsageHours", "SupportCalls"],
    outputCol="features"
)

prepared = assembler.transform(df)

train, test = prepared.randomSplit([0.8, 0.2], seed=42)

model = LogisticRegression(
    featuresCol="features",
    labelCol="label"
).fit(train)

predictions = model.transform(test)

predictions.select(
    "UsageHours", "SupportCalls", "label", "prediction"
).show()

evaluator = BinaryClassificationEvaluator()
print("Test AUC:", evaluator.evaluate(predictions))

spark.stop()

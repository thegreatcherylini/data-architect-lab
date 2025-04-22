# Databricks notebook source
from pyspark.sql import SparkSession

# Create a small sample DataFrame
data = [
    (1, "Cheryl", "Data Architect"),
    (2, "Jeb", "AI Companion"),
    (3, "Eric", "Field CTO"),
]
columns = ["id", "name", "role"]

df = spark.createDataFrame(data, columns)

# Write as Delta table to DBFS (Databricks File System)
df.write.format("delta").mode("overwrite").save("/tmp/sample_delta")

# COMMAND ----------

# Load the Delta table
delta_df = spark.read.format("delta").load("/tmp/sample_delta")

# Show the contents
delta_df.show()

# COMMAND ----------

spark.sql("DROP TABLE IF EXISTS sample_roles")

spark.sql("""
  CREATE TABLE sample_roles
  USING DELTA
  LOCATION '/tmp/sample_delta'
""")

# COMMAND ----------

spark.sql("SELECT * FROM sample_roles").show()
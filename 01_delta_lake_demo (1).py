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

# COMMAND ----------

# Step 1: Overwrite the delta table with updated values
updated_data = spark.createDataFrame(
    [(1, "Architect"), (2, "Companion"), (3, "CTO"), (4, "Product Manager")],
    ["id", "role"]
)

updated_data.write.format("delta").mode("overwrite").save("/tmp/sample_delta")

# COMMAND ----------

# Step 2: Use the DeltaTable utility to see version history
from delta.tables import DeltaTable
delta_table = DeltaTable.forPath(spark, "/tmp/sample_delta")
delta_table.history().show()

# COMMAND ----------

# Step 3: Query an older version of the table
df_old = spark.read.format("delta").option("versionAsOf", 0).load("/tmp/sample_delta")
df_old.show()

# COMMAND ----------

import os

# Make sure the tmp directory exists
os.makedirs("/dbfs/tmp", exist_ok=True)

# COMMAND ----------

import pandas as pd
import os

# Create a simple DataFrame
data = {
    "id": [1, 2, 3],
    "name": ["Ada", "Grace", "Cheryl"],
    "age": [34, 42, 29]
}
df = pd.DataFrame(data)

# Save it locally (Databricks driver node) as a CSV
csv_path = "/dbfs/tmp/people.csv"
df.to_csv(csv_path, index=False)

print(f"CSV written to {csv_path}")

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/tmp"))

# COMMAND ----------

# Convert pandas DataFrame to Spark DataFrame
spark_df = spark.createDataFrame(df)

# Save it as CSV to DBFS where Spark can read it
spark_df.write.mode("overwrite").option("header", True).csv("dbfs:/tmp/people_csv")

# COMMAND ----------

csv_df = spark.read.format("csv").option("header", "true").load("dbfs:/tmp/people_csv")
csv_df.show()

# COMMAND ----------

from pyspark.sql.functions import lit

# Add a new row to the Delta table
new_data = spark.createDataFrame([(4, "Jeb", "Principal AI")], ["id", "name", "role"])
new_data.write.format("delta").mode("append").save("/tmp/sample_delta")

# COMMAND ----------

spark.sql("DESCRIBE HISTORY delta.`/tmp/sample_delta`").show(truncate=False)

# COMMAND ----------

old_version_df = spark.read.format("delta").option("versionAsOf", 0).load("/tmp/sample_delta")
old_version_df.show()

# COMMAND ----------

from pyspark.sql.functions import lit

# Create new row to append
new_data = spark.createDataFrame([(4, "Jeb", "Principal AI")], ["id", "name", "role"])

# Append it to the Delta table
new_data.write.format("delta").mode("append").save("/tmp/sample_delta")

# COMMAND ----------

# Check history (Delta table versioning)
spark.sql("DESCRIBE HISTORY delta.`/tmp/sample_delta`").show(truncate=False)

# COMMAND ----------

# Query version 1
df_old = spark.read.format("delta").option("versionAsOf", 1).load("/tmp/sample_delta")
df_old.show()

# COMMAND ----------

import pandas as pd

# Sample data
data = {
    "name": ["Cheryl", "Amir", "Kai", "Lucia", "Jin"],
    "role": ["Architect", "Engineer", "Analyst", "Product Manager", "Data Scientist"],
    "department": ["Data", "Engineering", "Analytics", "Product", "AI/ML"]
}

df = pd.DataFrame(data)

# Save to DBFS
csv_path = "/dbfs/tmp/team_roster.csv"
df.to_csv(csv_path, index=False)

print(f"✅ CSV written to {csv_path}")

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/"))

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/FileStore/"))

# COMMAND ----------

csv_df = spark.read.format("csv") \
    .option("header", "true") \
    .load("dbfs:/FileStore/tmp/team_roster.csv")

csv_df.show()

# COMMAND ----------

# Load the CSV file into a Spark DataFrame
csv_df = spark.read.format("csv") \
    .option("header", "true") \
    .load("dbfs:/FileStore/tmp/team_roster.csv")

# Show the contents
csv_df.show()

# COMMAND ----------

# Save the CSV DataFrame as a Delta table
csv_df.write.format("delta") \
    .mode("overwrite") \
    .save("dbfs:/tmp/team_roster_delta")

# COMMAND ----------

# Read the Delta table
delta_df = spark.read.format("delta").load("dbfs:/tmp/team_roster_delta")
delta_df.show()


# COMMAND ----------

new_row.write.format("delta") \
    .option("mergeSchema", "true") \
    .mode("append") \
    .save("dbfs:/tmp/team_roster_delta")

# COMMAND ----------

# Query an older version of the Delta table
historical_df = spark.read.format("delta") \
    .option("versionAsOf", 0) \
    .load("dbfs:/tmp/team_roster_delta")

historical_df.show()
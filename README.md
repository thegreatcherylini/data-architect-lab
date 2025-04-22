# Delta Lake Demo (Databricks Community Edition)
![Databricks](https://img.shields.io/badge/Built%20With-Databricks-orange?logo=databricks)
![Delta Lake](https://img.shields.io/badge/Data%20Format-Delta%20Lake-blue?logo=apachespark)
![License: MIT](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Project-Active-brightgreen)

Welcome! This project demonstrates foundational data engineering tasks using Databricks, Delta Lake, and the Databricks File System (DBFS). It’s designed for practicing data architects who want hands-on experience with Delta Lake features in a collaborative notebook environment.

🧭 About This Project
This repository contains a guided hands-on lab exploring foundational data engineering tasks using Databricks Community Edition and Delta Lake. Designed for data architects and analytics professionals, it simulates real-world scenarios such as writing Delta tables, versioning data with Time Travel, and ingesting files into Spark using the Databricks File System (DBFS).

The goal of this project is to:

Strengthen familiarity with the Databricks Lakehouse platform

Practice data versioning, schema enforcement, and appends

Build confidence using notebooks and PySpark for exploratory and operational data workflows

This is the first in a series of small, practical projects designed to build and demonstrate architectural fluency in modern cloud-native data platforms.

## 🧱 What’s Included

- Create and query a Delta table
- Use Time Travel to explore table versions
- Save CSV data to DBFS and load it into Spark
- Append data and observe schema enforcement
- Push notebooks to GitHub and organize your project

## 📁 Folder Structure

├── 01_delta_lake_demo.py # Main notebook with Spark + Delta Lake code ├── team_roster.csv # Example CSV uploaded to DBFS ├── README.md # You’re here! ├── LICENSE └── Untitled Diagram.drawio # ERD / architecture sketch (optional)

pgsql
Copy
Edit

## 🧪 Technologies Used

- Databricks Community Edition
- Delta Lake
- Apache Spark
- Python (PySpark)
- DBFS (Databricks File System)

## 🚀 How to Use

1. Clone the repo or open the notebook directly in Databricks
2. Run all cells in `01_delta_lake_demo.py`
3. Upload your own data to DBFS if you’d like to try variations
4. Check Delta history, test schema enforcement, and explore Time Travel

## 💡 Notes

- Time Travel is a built-in feature of Delta tables — experiment with it using `DESCRIBE HISTORY`
- Schema mismatch errors (like when appending new data) are a great opportunity to test `.option("mergeSchema", "true")`
- This project uses **Databricks Community Edition**, which is free to try and great for testing!

## 🧑🏾‍💻 Author

**Cheryl Wink, PhD**  
Cloud Data Architect | Data Engineering Leader | Snowflake + Databricks Advocate  
[LinkedIn](https://www.linkedin.com/in/cherylwink) | [GitHub](https://github.com/thegreatcherylini)

---

This is a living lab. Pull requests, improvements, and ideas welcome!

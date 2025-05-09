# Delta Lake Demo (Databricks Community Edition)
![Databricks](https://img.shields.io/badge/Built%20With-Databricks-orange?logo=databricks)
![Delta Lake](https://img.shields.io/badge/Data%20Format-Delta%20Lake-blue?logo=apachespark)
![License: MIT](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Project-Active-brightgreen)

🧭 About This Project

Welcome! This project demonstrates foundational data engineering tasks using Databricks, Delta Lake, and the Databricks File System (DBFS). It’s designed for practicing data architects who want hands-on experience with Delta Lake features in a collaborative notebook environment.

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

## 🗺️ Project Roadmap

This lab is part of a broader initiative to strengthen architectural intuition through hands-on experimentation with modern data platforms.

| Milestone | Description |
|-----------|-------------|
| ✅ Phase 1: Delta Lake Fundamentals | Create, query, time travel, and update Delta tables using Databricks Community Edition |
| 🔄 Phase 2: Streaming & Joins | Implement structured streaming and join Delta tables for enriched analytics workflows |
| ⏳ Phase 3: Orchestration & Pipelines | Introduce notebook workflows and pipeline orchestration with Databricks Jobs |
| 🧪 Phase 4: Data Quality Checks | Add data validation with tools like `expectations` or simple custom checks |
| 🔒 Phase 5: Governance Concepts | Apply Unity Catalog concepts (in full Databricks version) and explore RBAC patterns |
| 📊 Phase 6: BI + Visualization | Connect outputs to Power BI or Tableau; experiment with dashboards and data products |
| 🚀 Phase 7: Cloud Integration | Extend to Azure or AWS with real blob storage for enterprise-scale workflows |

💡 *This roadmap is intentionally modular so each notebook can stand alone as a focused learning experience.*

## ⚙️ Setup & Usage

This project runs entirely in **Databricks Community Edition**—no paid cloud account required.

### 1. 🚀 Get Started
- Sign up at [Databricks Community Edition](https://community.cloud.databricks.com)
- Create a new notebook and attach it to a running cluster
- Clone or copy the notebook code from this repo into your Databricks workspace

### 2. 📁 Upload Data
- Use the `Upload Data` button in Databricks to upload sample CSVs to DBFS
- For example: `/dbfs/tmp/team_roster.csv`

### 3. 🧪 Run the Notebook
- Load CSVs into Spark DataFrames
- Save and query Delta tables
- Use `DESCRIBE HISTORY` to explore Time Travel

### 4. 🔁 Experiment
- Try appending new rows, updating values, or rewriting the table
- Enable schema evolution with `.option("mergeSchema", "true")` on writes
- Practice version control with GitHub by pushing your notebook updates

---

📌 *No local setup needed—this project is entirely cloud-hosted for simplicity and speed.*

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

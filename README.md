# E-Commerce Store Analytics Sync Pipeline

A production-ready batch ETL pipeline orchestrated with Apache Airflow inside Docker. This system automates the ingestion of daily transactional sales records, processes currency transformations from USD to EUR, computes regional value-added tax (VAT), and outputs structured data ready for analytics consumption.

## 📐 Architecture Overview
The workflow is containerized using Docker Compose running an Airflow Standalone environment. The execution flow follows a strict dependency hierarchy:
`Starting_the_pipeline` ➔ `generate_orders_transactions` ➔ `transform_data` ➔ `end_pipeline`

## 📁 Directory Structure
```text
e-commerce store analytic sync/
├── dags/
│   ├── ecommerce_analytics_dag.py  # Master DAG Orchestrator
│   ├── generate_raw_data.py        # Simulated entry stream ingestion
│   └── transform_data.py           # ETL logic (Math, types, and structuring)
├── data/
│   ├── raw_data.csv                # Extracted transactional layer
│   └── transformed_data.csv        # Normalized analytics output layer
└── docker-compose.yaml             # Container orchestration layer

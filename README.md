# superstore_data_portfolio

This project demonstrates data cleaning, exploratory data analysis (EDA) with Python, and data querying with SQL using a sample "Superstore" dataset.

## Project Structure

superstore_portfolio/
├── data/
│ ├── superstore.csv # Original raw data
│ └── superstore_cleaned.csv # Cleaned data output from 01_data_cleaning.py
├── scripts/
│ ├── 01_data_cleaning.py
│ ├── 02_exploratory_data_analysis.py
│ ├── 03_sql_database_load.py
│ └── 04_sql_queries.sql
├── output/ # Outputs from analysis scripts
│ ├── sales_profit_trend.png # Example plot from EDA
│ ├── top_products.png # Example plot from EDA
│ ├── eda_console_output.txt # Console output from 02_exploratory_data_analysis.py
│ └── sql_query_results.txt # Results copied from DB Browser for SQLite
├── database/
│ └── superstore.db # SQLite database created by 03_sql_database_load.py
└── README.md # This file

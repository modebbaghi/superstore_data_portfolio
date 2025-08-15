# Superstore Data Analysis Portfolio

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


## Technologies Used

*   Python (pandas, matplotlib, seaborn)
*   SQLite
*   DB Browser for SQLite (for running SQL queries)

## How to Run

1.  Ensure Python and required libraries (`pandas`, `matplotlib`, `seaborn`) are installed. You can install them using `pip install pandas matplotlib seaborn`.
2.  Navigate to the `scripts` directory in your terminal/command prompt.
3.  Run the scripts in order:
    *   `python 01_data_cleaning.py`: Cleans the data and saves `superstore_cleaned.csv` in the `data` folder.
    *   `python 02_exploratory_data_analysis.py`: Generates plots (saved in `output`) and prints summary statistics.
    *   `python 03_sql_database_load.py`: Loads `superstore_cleaned.csv` into `superstore.db` in the `database` folder.
4.  Use DB Browser for SQLite to open `database/superstore.db`.
5.  Execute the queries from `scripts/04_sql_queries.sql` in DB Browser. Copy the results for key queries into `output/sql_query_results.txt`.

## Key Findings (Optional but Good)

*   Briefly summarize interesting insights discovered during EDA or SQL analysis.
*   Example: "Office Supplies is the highest-selling category." "The West region generates the most profit."

## Outputs

*   **EDA Plots:** See `output/` folder for generated visualizations.
*   **EDA Summary:** See `output/eda_console_output.txt`.
*   **SQL Results:** See `output/sql_query_results.txt`.
*   **Database:** The final database is located at `database/superstore.db`.

# 🌟 Data Analyst Portfolio

## 📊 Dashboard Projects
- [Sales Performance Dashboard](dashboard_design.md) - Interactive Tableau dashboard with real-time insights

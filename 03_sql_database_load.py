# portfolio_step3a_sql_load.py

import sqlite3
import pandas as pd

# Load the cleaned data
# --- Define Path for Cleaned Data ---
import os
# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Get the parent directory (Portfolio/Superstore)
parent_dir = os.path.dirname(script_dir)
# Construct the path to the data folder and the file
data_file_path = os.path.join(parent_dir, 'data', 'superstore_cleaned.csv')

# --- Load the cleaned data ---
df = pd.read_csv(data_file_path)
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Ship_Date'] = pd.to_datetime(df['Ship_Date'])

# Connect to SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect('superstore.db')

# Write the DataFrame to a table named 'sales'
df.to_sql('sales', conn, if_exists='replace', index=False)

# Commit changes and close connection
conn.commit()
conn.close()

print("Data loaded into SQLite database 'superstore.db' in table 'sales'")

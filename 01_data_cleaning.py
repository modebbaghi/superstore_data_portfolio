# 01_data_cleaning.py (Corrected for single-record-per-line format)

import pandas as pd
import os

# --- Define Paths ---
# This script is in 'scripts', data is in '../data'
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
data_dir = os.path.join(parent_dir, 'data')
input_file_path = os.path.join(data_dir, 'superstore.csv')
output_file_path = os.path.join(data_dir, 'superstore_cleaned.csv')

# --- Check if input file exists ---
if not os.path.exists(input_file_path):
    print(f"Error: Input file not found at {input_file_path}")
    exit()

print(f"Loading data from: {input_file_path}")

# --- Define correct column names for single-record format ---
column_names = [
    'Row_ID', 'Order_ID', 'Order_Date', 'Ship_Date', 'Ship_Mode',
    'Customer_ID', 'Customer_Name', 'Segment', 'Country', 'City',
    'State', 'Postal_Code', 'Region', 'Product_ID', 'Category',
    'Sub_Category', 'Product_Name', 'Sales', 'Quantity', 'Discount', 'Profit'
]

# --- Load the data ---
encodings_to_try = ['cp1252', 'latin1', 'utf-8']
df_clean = None
last_error = None

for encoding in encodings_to_try:
    try:
        print(f"Trying to load data with encoding: {encoding}")
        df_clean = pd.read_csv(
            input_file_path,
            sep=';', # Use semicolon as separator
            header=None, # No header row in the file
            names=column_names, # Assign column names
            dtype=str, # Read everything as string first
            encoding=encoding,
            on_bad_lines='skip' # Skip lines with issues
        )
        print(f"Success! Raw data loaded with encoding '{encoding}'. Shape: {df_clean.shape}")
        break
    except UnicodeDecodeError as e:
        print(f"Failed to load with encoding '{encoding}': {e}")
        last_error = e
    except Exception as e:
        print(f"An unexpected error occurred while loading with encoding '{encoding}': {e}")
        last_error = e
        break

if df_clean is None:
    print(f"Error loading data: Could not decode file with any of the attempted encodings {encodings_to_try}.")
    print(f"Last error encountered: {last_error}")
    exit()


# --- Data Type Conversion ---
try:
    # Convert date columns
    df_clean['Order_Date'] = pd.to_datetime(df_clean['Order_Date'], format='%d/%m/%Y', errors='coerce')
    df_clean['Ship_Date'] = pd.to_datetime(df_clean['Ship_Date'], format='%d/%m/%Y', errors='coerce')

    # Convert numeric columns (replace comma with dot for decimal)
    numeric_cols = ['Sales', 'Quantity', 'Discount', 'Profit']
    for col in numeric_cols:
        if col in df_clean.columns:
             df_clean[col] = pd.to_numeric(df_clean[col].astype(str).str.replace(',', '.'), errors='coerce')

    print("Data types converted.")
except Exception as e:
    print(f"Warning: Error during data type conversion: {e}")

# --- Final Cleaning ---
# Drop rows with missing critical data (e.g., Order_ID, Sales)
initial_rows = len(df_clean)
df_clean.dropna(subset=['Order_ID', 'Sales'], inplace=True)
final_rows = len(df_clean)
print(f"Dropped {initial_rows - final_rows} rows due to missing Order_ID or Sales.")

# Reset index after dropping rows
df_clean.reset_index(drop=True, inplace=True)

# --- Save Cleaned Data ---
try:
    df_clean.to_csv(output_file_path, index=False)
    print(f"Data cleaning complete! Cleaned data saved to: {output_file_path}")
except Exception as e:
    print(f"Error saving cleaned data: {e}")
    exit()

# Display basic info
print("\n--- Data Sample ---")
print(df_clean.head())
print("\n--- Data Info ---")
print(df_clean.info())
print("\n--- Data Description ---")
print(df_clean.describe(include='all'))

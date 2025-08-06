# portfolio_step2_eda.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# --- Basic Statistics ---
print("--- Sales Summary ---")
print(f"Total Sales: ${df['Sales'].sum():,.2f}")
print(f"Total Profit: ${df['Profit'].sum():,.2f}")
print(f"Average Order Value: ${df.groupby('Order_ID')['Sales'].sum().mean():,.2f}")
print(f"Number of Orders: {df['Order_ID'].nunique()}")
print(f"Number of Customers: {df['Customer_ID'].nunique()}")
print(f"Number of Products: {df['Product_ID'].nunique()}")

# --- Visualizations ---
# 1. Sales and Profit over Time (Monthly)
df['Order_Month'] = df['Order_Date'].dt.to_period('M')
monthly_sales = df.groupby('Order_Month')['Sales'].sum()
monthly_profit = df.groupby('Order_Month')['Profit'].sum()

fig, ax1 = plt.subplots(figsize=(12, 6))
color = 'tab:blue'
ax1.set_xlabel('Month')
ax1.set_ylabel('Sales ($)', color=color)
ax1.plot(monthly_sales.index.astype(str), monthly_sales.values, color=color, marker='o', label='Sales')
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_xticklabels(monthly_sales.index.astype(str), rotation=45, ha='right')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
color = 'tab:orange'
ax2.set_ylabel('Profit ($)', color=color)  # we already handled the x-label with ax1
ax2.plot(monthly_profit.index.astype(str), monthly_profit.values, color=color, marker='s', label='Profit')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.title('Monthly Sales and Profit')
plt.show()

# 2. Sales by Category and Sub-Category
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x=category_sales.values, y=category_sales.index, palette='viridis')
plt.title('Total Sales by Category')
plt.xlabel('Sales ($)')
plt.ylabel('Category')
plt.show()

subcategory_sales = df.groupby(['Category', 'Sub_Category'])['Sales'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 8))
sns.barplot(x=subcategory_sales.values, y=[f"{cat} - {sub}" for cat, sub in subcategory_sales.index], palette='magma')
plt.title('Top 10 Sales by Sub-Category')
plt.xlabel('Sales ($)')
plt.ylabel('Category - Sub-Category')
plt.show()

# 3. Profit by Region
region_profit = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 6))
sns.barplot(x=region_profit.values, y=region_profit.index, palette='coolwarm')
plt.title('Total Profit by Region')
plt.xlabel('Profit ($)')
plt.ylabel('Region')
plt.show()

# 4. Top 10 Products by Sales
top_products = df.groupby('Product_Name')['Sales'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 8))
sns.barplot(x=top_products.values, y=top_products.index, palette='rocket')
plt.title('Top 10 Products by Sales')
plt.xlabel('Sales ($)')
plt.ylabel('Product Name')
plt.show()

# 5. Correlation between Quantity, Discount, and Profit
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Quantity', y='Discount', hue='Profit', palette='coolwarm', alpha=0.7)
plt.title('Quantity vs Discount (colored by Profit)')
plt.xlabel('Quantity')
plt.ylabel('Discount')
plt.legend(title='Profit')
plt.show()

print("\n--- EDA Complete ---")
# You can add more analysis here (e.g., customer analysis, shipping analysis)

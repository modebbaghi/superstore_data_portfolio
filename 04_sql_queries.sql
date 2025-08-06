-- portfolio_step3b_sql_queries.sql

-- Use the superstore.db database (in SQLite CLI or DB Browser)
-- .open superstore.db

-- 1. Basic SELECT and Aggregation
-- Find total sales, profit, and number of orders
SELECT
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    COUNT(DISTINCT Order_ID) AS Number_of_Orders
FROM sales;

-- 2. Filtering and Sorting
-- Top 10 customers by total sales
SELECT
    Customer_ID,
    Customer_Name,
    SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Customer_ID, Customer_Name
ORDER BY Total_Sales DESC
LIMIT 10;

-- 3. Grouping and Aggregation with HAVING
-- Categories with average profit margin > 10%
SELECT
    Category,
    AVG(Profit / NULLIF(Sales, 0)) AS Avg_Profit_Margin -- Handle division by zero
FROM sales
WHERE Sales > 0
GROUP BY Category
HAVING Avg_Profit_Margin > 0.10;

-- 4. Date-based Analysis
-- Monthly sales trend for the last 2 years (assuming data covers it)
-- Note: Date functions might vary slightly depending on SQL dialect
SELECT
    strftime('%Y-%m', Order_Date) AS Order_Month, -- SQLite specific
    SUM(Sales) AS Monthly_Sales
FROM sales
WHERE Order_Date >= date('now', '-2 years') -- SQLite specific
GROUP BY Order_Month
ORDER BY Order_Month;

-- 5. Join-like operation using Subquery (Find top selling product in each category)
-- This is a common pattern in SQL interviews
SELECT
    s1.Category,
    s1.Product_Name,
    s1.Product_Sales
FROM (
    SELECT
        Category,
        Product_Name,
        SUM(Sales) AS Product_Sales
    FROM sales
    GROUP BY Category, Product_Name
) AS s1
WHERE s1.Product_Sales = (
    SELECT MAX(s2.Product_Sales)
    FROM (
        SELECT
            Category,
            Product_Name,
            SUM(Sales) AS Product_Sales
        FROM sales s3
        WHERE s3.Category = s1.Category
        GROUP BY Category, Product_Name
    ) AS s2
)
ORDER BY s1.Category;

-- 6. Window Functions (if supported by your SQL engine, e.g., SQLite 3.25+)
-- Rank products within each category by sales
SELECT
    Category,
    Product_Name,
    SUM(Sales) AS Product_Sales,
    ROW_NUMBER() OVER (PARTITION BY Category ORDER BY SUM(Sales) DESC) AS Sales_Rank
FROM sales
GROUP BY Category, Product_Name
ORDER BY Category, Sales_Rank;

-- 7. Conditional Aggregation
-- Sales and profit breakdown by Segment
SELECT
    Segment,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    SUM(CASE WHEN Profit < 0 THEN 1 ELSE 0 END) AS Num_Loss_Making_Orders,
    COUNT(*) AS Total_Orders
FROM sales
GROUP BY Segment;

-- 8. Complex Filter
-- Find orders where the customer bought both 'Office Supplies' and 'Furniture' in the same order
-- This requires joining the table with itself or using EXISTS
SELECT DISTINCT s1.Order_ID
FROM sales s1
WHERE s1.Category = 'Office Supplies'
AND EXISTS (
    SELECT 1
    FROM sales s2
    WHERE s2.Order_ID = s1.Order_ID
    AND s2.Category = 'Furniture'
);

-- 9. String Operations (Find products with 'Xerox' in the name)
SELECT DISTINCT Product_Name, Category, Sub_Category
FROM sales
WHERE Product_Name LIKE '%Xerox%';

-- 10. Performance Consideration (Indexing)
-- While not a SELECT query, showing index creation is important
-- Create an index on frequently queried columns like Order_Date or Category
CREATE INDEX IF NOT EXISTS idx_order_date ON sales(Order_Date);
CREATE INDEX IF NOT EXISTS idx_category ON sales(Category);
-- Remember to analyze query plans to see if indexes are used.

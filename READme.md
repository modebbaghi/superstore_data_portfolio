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




Xerox 1967	Office Supplies	Paper
Xerox 232	Office Supplies	Paper
Xerox 1943	Office Supplies	Paper
Xerox 1995	Office Supplies	Paper
Xerox 1999	Office Supplies	Paper
Xerox 1921	Office Supplies	Paper
Xerox 1916	Office Supplies	Paper
Xerox 195	Office Supplies	Paper
Xerox 1880	Office Supplies	Paper
Xerox 1911	Office Supplies	Paper
Xerox 1883	Office Supplies	Paper
Xerox 1920	Office Supplies	Paper
Xerox 1913	Office Supplies	Paper
Xerox 205	Office Supplies	Paper
Xerox 4200 Series MultiUse Premium Copy Paper (20Lb. and 84 Bright)	Office Supplies	Paper
Xerox 1957	Office Supplies	Paper
Xerox WorkCentre 6505DN Laser Multifunction Printer	Technology	Machines
Xerox 216	Office Supplies	Paper
Xerox 223	Office Supplies	Paper
Xerox 1939	Office Supplies	Paper
Xerox 21	Office Supplies	Paper
Xerox 1881	Office Supplies	Paper
Xerox 1930	Office Supplies	Paper
Xerox 1960	Office Supplies	Paper
Xerox 1958	Office Supplies	Paper
Xerox 1974	Office Supplies	Paper
Xerox 1908	Office Supplies	Paper
Xerox 191	Office Supplies	Paper
Xerox 1987	Office Supplies	Paper
Xerox 1897	Office Supplies	Paper
Xerox Color Copier Paper, 11" x 17", Ream	Office Supplies	Paper
Xerox 1912	Office Supplies	Paper
Xerox 1898	Office Supplies	Paper
Xerox 226	Office Supplies	Paper
Xerox 222	Office Supplies	Paper
Xerox 225	Office Supplies	Paper
Xerox 1894	Office Supplies	Paper
Xerox 1889	Office Supplies	Paper
Xerox 1972	Office Supplies	Paper
Xerox 1993	Office Supplies	Paper
Xerox 1977	Office Supplies	Paper
Xerox 220	Office Supplies	Paper
Xerox 1964	Office Supplies	Paper
Xerox 196	Office Supplies	Paper
Xerox 1927	Office Supplies	Paper
Xerox 1887	Office Supplies	Paper
Xerox 218	Office Supplies	Paper
Xerox 1968	Office Supplies	Paper
Xerox 1941	Office Supplies	Paper
Xerox 202	Office Supplies	Paper
Xerox 1884	Office Supplies	Paper
Xerox 1910	Office Supplies	Paper
Xerox 1923	Office Supplies	Paper
Xerox 1931	Office Supplies	Paper
Xerox 1985	Office Supplies	Paper
Xerox 213	Office Supplies	Paper
Xerox 210	Office Supplies	Paper
Xerox 212	Office Supplies	Paper
Xerox 188	Office Supplies	Paper
Xerox 1979	Office Supplies	Paper
Xerox 2	Office Supplies	Paper
Xerox 1935	Office Supplies	Paper
Xerox 224	Office Supplies	Paper
Xerox 1950	Office Supplies	Paper
Xerox 1905	Office Supplies	Paper
Xerox 1945	Office Supplies	Paper
Xerox 1896	Office Supplies	Paper
Xerox 1996	Office Supplies	Paper
Xerox 1924	Office Supplies	Paper
Xerox 1915	Office Supplies	Paper
Xerox 1973	Office Supplies	Paper
Xerox 1909	Office Supplies	Paper
Xerox 1934	Office Supplies	Paper
Xerox 217	Office Supplies	Paper
Xerox 189	Office Supplies	Paper
Xerox 203	Office Supplies	Paper
Xerox 1948	Office Supplies	Paper
Xerox 1946	Office Supplies	Paper
Xerox 192	Office Supplies	Paper
Xerox 199	Office Supplies	Paper
Xerox 197	Office Supplies	Paper
Xerox 1970	Office Supplies	Paper
Xerox 1988	Office Supplies	Paper
Xerox 1949	Office Supplies	Paper
Xerox 1886	Office Supplies	Paper
Xerox 1901	Office Supplies	Paper
Xerox 1940	Office Supplies	Paper
Xerox 1986	Office Supplies	Paper
Xerox 1925	Office Supplies	Paper
Xerox 231	Office Supplies	Paper
Xerox 1962	Office Supplies	Paper
Xerox 1919	Office Supplies	Paper
Xerox 1929	Office Supplies	Paper
Xerox 206	Office Supplies	Paper
Xerox 1998	Office Supplies	Paper
Xerox 1981	Office Supplies	Paper
Xerox 211	Office Supplies	Paper
Xerox 1891	Office Supplies	Paper
Xerox 214	Office Supplies	Paper
Xerox 1978	Office Supplies	Paper
Xerox 1922	Office Supplies	Paper
Xerox 1952	Office Supplies	Paper
Xerox 1888	Office Supplies	Paper
Xerox 1982	Office Supplies	Paper
Xerox 1991	Office Supplies	Paper
Xerox 1959	Office Supplies	Paper
Xerox 22	Office Supplies	Paper
Xerox 1989	Office Supplies	Paper
Xerox 1984	Office Supplies	Paper
Xerox 227	Office Supplies	Paper
Xerox 1965	Office Supplies	Paper
Xerox 1994	Office Supplies	Paper
Xerox 1926	Office Supplies	Paper
Xerox 1918	Office Supplies	Paper
Xerox 1951	Office Supplies	Paper
Xerox 219	Office Supplies	Paper
Xerox 1903	Office Supplies	Paper
Xerox 23	Office Supplies	Paper
Xerox 1895	Office Supplies	Paper
Xerox 2000	Office Supplies	Paper
Xerox 1944	Office Supplies	Paper
Xerox 215	Office Supplies	Paper
Xerox 1885	Office Supplies	Paper
Xerox 1953	Office Supplies	Paper
Xerox 228	Office Supplies	Paper
Xerox 1954	Office Supplies	Paper
Xerox 1942	Office Supplies	Paper
Xerox 201	Office Supplies	Paper
Xerox 1969	Office Supplies	Paper
Xerox 1971	Office Supplies	Paper
Xerox 198	Office Supplies	Paper
Xerox 1997	Office Supplies	Paper
Xerox 230	Office Supplies	Paper
Xerox 194	Office Supplies	Paper
Xerox 1980	Office Supplies	Paper
Xerox 1907	Office Supplies	Paper
Xerox 221	Office Supplies	Paper
Xerox 1893	Office Supplies	Paper
Xerox 1900	Office Supplies	Paper
Xerox 204	Office Supplies	Paper
Xerox 200	Office Supplies	Paper
Xerox 1882	Office Supplies	Paper
Xerox 1966	Office Supplies	Paper
Xerox 1928	Office Supplies	Paper
Xerox 1890	Office Supplies	Paper
Xerox 1990	Office Supplies	Paper
Xerox 1933	Office Supplies	Paper
Xerox 1975	Office Supplies	Paper
Xerox 208	Office Supplies	Paper
Xerox 1992	Office Supplies	Paper
Xerox 190	Office Supplies	Paper
Xerox 1892	Office Supplies	Paper
Xerox 1956	Office Supplies	Paper
Xerox 1937	Office Supplies	Paper
Xerox 1917	Office Supplies	Paper
Xerox 19	Office Supplies	Paper
Xerox 1932	Office Supplies	Paper
Xerox 209	Office Supplies	Paper
Xerox 1906	Office Supplies	Paper
Xerox 1963	Office Supplies	Paper
Xerox 20	Office Supplies	Paper
Xerox 1914	Office Supplies	Paper
Xerox 1902	Office Supplies	Paper
Xerox 207	Office Supplies	Paper
Xerox 1947	Office Supplies	Paper
Xerox 193	Office Supplies	Paper
Xerox 1936	Office Supplies	Paper
Xerox 229	Office Supplies	Paper
Xerox 1976	Office Supplies	Paper
Xerox 1983	Office Supplies	Paper
Xerox 1938	Office Supplies	Paper
Xerox 1899	Office Supplies	Paper
Xerox 1955	Office Supplies	Paper
Xerox Blank Computer Paper	Office Supplies	Paper

import sqlite3
import pandas as pd


# Establish connection to the SQLite database
conn = sqlite3.connect('data/instamart.db')

# Read queries from sql/queries.sql
with open('sql/queries.sql', 'r') as f:
    sql_script = f.read()

# Split queries by semicolon
queries = [q.strip() for q in sql_script.split(';') if q.strip()]

# 1. Pivot Table with margins=True
orders_df = pd.read_sql_query(queries[1], conn)

pivot_result = pd.pivot_table(
    orders_df,
    values='order_amount',
    index='city',
    aggfunc=['sum', 'mean', 'count'],
    margins=True,
    margins_name='Grand Total'
)
print("--- Pivot Table Results ---")
print(pivot_result)

# 2. Groupby with Named Aggregation
groupby_result = orders_df.groupby('city').agg(
    total_sum=('order_amount', 'sum'),
    mean_amount=('order_amount', 'mean'),
    order_count=('order_amount', 'count')
)
print("\n--- Groupby Named Aggregation ---")
print(groupby_result)

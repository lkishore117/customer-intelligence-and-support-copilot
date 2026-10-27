import sqlite3
import pandas as pd


# Establish connection to the SQLite database
conn = sqlite3.connect('data/instamart.db')

# Read queries from sql/queries.sql
with open('sql/queries.sql', 'r') as f:
    sql_script = f.read()

# Split queries by semicolon
queries = [q.strip() for q in sql_script.split(';') if q.strip()]

# Execute and report results for each query
for idx, query in enumerate(queries, 1):
    df = pd.read_sql_query(query, conn)
    print(f"=== Q{idx} Output ===")
    print(f"Total Rows: {len(df)}")
    print(df.head(3))
    print("\n" + "=" * 50 + "\n")

conn.close()

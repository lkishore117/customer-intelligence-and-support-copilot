import os
import sqlite3

from dataframes import pd, customers_df, products_df, orders_df
from clean_customers import clean_customers
from clean_orders import clean_orders


def validate(customers_df, orders_df):
    validations = [
        ("Customers from Pune", customers_df.loc[customers_df['city'] == "pune"]['city'].count(), 227),
        ("Customers from Delhi", customers_df.loc[customers_df['city'] == "delhi"]['city'].count(), 210),
        ("Customers from Bengaluru", customers_df.loc[customers_df['city'] == "bengaluru"]['city'].count(), 197),
        ("Customers from Chennai", customers_df.loc[customers_df['city'] == "chennai"]['city'].count(), 191),
        ("Customers from Hyderabad", customers_df.loc[customers_df['city'] == "hyderabad"]['city'].count(), 191),
        ("Customers from Mumbai", customers_df.loc[customers_df['city'] == "mumbai"]['city'].count(), 184),
        ("Customers Gender - Female", customers_df.loc[customers_df['gender'] == "female"]['gender'].count(), 610),
        ("Customers Gender - Male", customers_df.loc[customers_df['gender'] == "male"]['gender'].count(), 560),
        ("Customers Gender - Unknown", customers_df.loc[customers_df['gender'] == "unknown"]['gender'].count(), 30),
        ("Customers Age Unknown", customers_df.loc[customers_df['age'].isnull()]['age'].count(), 0),
        ("Customers Age Between 18 and 60", customers_df.loc[(customers_df['age'] >= 18) & (customers_df['age'] <= 60)]['age'].count(), len(customers_df)),
        ("Orders Unique id", len(orders_df["order_id"].unique()), 12309),
        ("Orders Completed", len(orders_df[orders_df['status'] == 'completed']), 11110),
        ("Orders Cancelled", len(orders_df[orders_df['status'] == 'cancelled']), 1199),
        ("Orders Pending", len(orders_df[orders_df['status'] == 'pending']), 0),
        ("Orders Missing Amount", orders_df['order_amount'].isna().sum(), 0),
        ("Orders Missing Delivery Minutes among Completed", orders_df[orders_df['status'] == 'completed']["delivery_minutes"].isna().sum(), 0),
        ("Orders Missing Delivery Minutes among Cancelled", orders_df[orders_df['status'] == 'cancelled']["delivery_minutes"].isna().sum(), 1199),
        ("Orders Total Amount of Completed", orders_df[orders_df['status'] == 'completed']["order_amount"].sum(),  2998668.8)
    ]
    flag = True
    for validation in validations:
        f = validation[1] == validation[2]
        if not f:
            flag = False

    if flag:
        print('ALL CHECKPOINTS PASSED')
    else:
        print("SOME CHECKPOINTS FAILED")

customers_df = clean_customers(customers_df)
orders_df, products_df = clean_orders(orders_df, products_df)

os.makedirs('data/clean', exist_ok=True)

# Format order_ts as YYYY-MM-DD HH:MM:SS
orders_df['order_ts'] = pd.to_datetime(orders_df['order_ts']).dt.strftime('%Y-%m-%d %H:%M:%S')

# Save to CSV in data/clean/
customers_df.to_csv('data/clean/customers.csv', index=False)
products_df.to_csv('data/clean/products.csv', index=False)
orders_df.to_csv('data/clean/orders.csv', index=False)

# Save to SQLite database data/instamart.db
db_path = 'data/instamart.db'
conn = sqlite3.connect(db_path)

customers_df.to_sql('customers', conn, if_exists='replace', index=False)
products_df.to_sql('products', conn, if_exists='replace', index=False)
orders_df.to_sql('orders', conn, if_exists='replace', index=False)

conn.close()

# Validation Script
print("\n\n\n")
print('=' * 50)
print('VALIDATIONS:')
print('=' * 50)
validate(customers_df, orders_df)
print('=' * 50)

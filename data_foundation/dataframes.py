import pandas as pd

customers_df = pd.read_csv("data/raw/customers.csv")
products_df = pd.read_csv("data/raw/products.csv")
orders_df = pd.read_csv("data/raw/orders.csv")

tickets_df = pd.read_csv("data/raw/tickets.csv", keep_default_na=False)

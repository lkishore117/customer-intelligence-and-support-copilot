import numpy as np
from dataframes import pd, orders_df, products_df


def clean_orders(orders_df, products_df, ret=True):
    """ Convert order_ts to a datetime """
    orders_df["order_ts"] = pd.to_datetime(orders_df["order_ts"])

    """ Remove exact duplicate rows """
    orders_df = orders_df.drop_duplicates()

    """ Keep one record per order_id """
    orders_df = orders_df.sort_values(by=['order_id', 'order_ts']).drop_duplicates(subset=['order_id'], keep='last').reset_index(drop=True)

    """ Standardize order_amount field """
    orders_df['order_amount'] = pd.to_numeric(orders_df['order_amount'], errors='coerce')
    merged_df = pd.merge(orders_df, products_df, on="product_id", how="left")
    calc_amount = np.round(merged_df["price_inr"] * merged_df["quantity"] * (1 - merged_df["discount_pct"] / 100), 2)
    orders_df['order_amount'] = orders_df['order_amount'].fillna(calc_amount)

    """ Standardize delivery_minutes field """
    orders_df.loc[orders_df["delivery_minutes"] < 0, "delivery_minutes"] = np.nan
    merged_df = pd.merge(orders_df, products_df, on="product_id", how="left")
    completed_median = merged_df['delivery_minutes'].where(merged_df['status'] == 'completed').groupby(merged_df['category']).transform('median')
    completed_fill_mask = (merged_df['status'] == 'completed') & (merged_df['delivery_minutes'].isna())
    merged_df.loc[completed_fill_mask, 'delivery_minutes'] = completed_median[completed_fill_mask]
    orders_df['delivery_minutes'] = merged_df['delivery_minutes']

    if ret:
        return (orders_df, products_df)


clean_orders(orders_df, products_df)

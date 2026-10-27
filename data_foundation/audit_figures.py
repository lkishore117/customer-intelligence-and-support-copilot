from dataframes import pd, orders_df, customers_df


print("\n\n\n")
print('=' * 50)
print('AUDIT FIGURES:')
print('=' * 50)
print(pd.Series({
    "orders_row": len(orders_df),
    "orders_exact_duplicates": len(orders_df) - len(orders_df.drop_duplicates()),
    "orders_pending": len(orders_df[orders_df["status"] == 'pending']),
    "orders_unique_order_ids": len(orders_df["order_id"].unique()),
    "orders_non_numeric_amount": len(orders_df) - pd.to_numeric(orders_df["order_amount"], errors="coerce").count(),
    "orders_negative_delivery_minutes": orders_df[orders_df["delivery_minutes"] < 0]["delivery_minutes"].count(),
    "orders_blank_delivery_minutes": len(orders_df) - orders_df["delivery_minutes"].count(),
    "customers_blank_age": len(customers_df) - customers_df["age"].count(),
    "customers_age_outside_limit": ((customers_df["age"] < 10) | (customers_df["age"] > 100)).sum(),
    "customers_distinct_city": len(customers_df["city"].unique()),
    "customers_distinct_gender_nonnull": len(customers_df[customers_df["gender"].notnull()]["gender"].unique()),
    "customers_blank_gender": customers_df["gender"].isnull().sum()
}))
print('=' * 50)

from dataframes import pd, orders_df, customers_df, products_df


def get_df_details(df: pd.DataFrame):
    columns = []
    dtypes = []
    nonnulls = []
    sizes = []
    missing_percents = []
    for column in df.columns:
        col_series = df[column]
        columns.append(column)
        dtypes.append(col_series.dtype)
        nonnulls.append(col_series.count())
        sizes.append(col_series.size)
        missing_percents.append(float(f"{100 - (col_series.count() * 100 / col_series.size) : .2f}"))
    return pd.DataFrame({
        "column": columns,
        "data_type": dtypes,
        "non_null": nonnulls,
        "size": sizes,
        "missing_percent": missing_percents
    })


print("\n\n\n")
print('=' * 50)
print('MISSING DETAILS:')
print('=' * 50)
print('-' * 50)
print("Customers:")
print('-' * 50)
print(get_df_details(customers_df), end="\n\n")
print('-' * 50)
print("Products:")
print('-' * 50)
print(get_df_details(products_df), end="\n\n")
print('-' * 50)
print("Orders:")
print('-' * 50)
print(get_df_details(orders_df), end="\n\n")
print('=' * 50)

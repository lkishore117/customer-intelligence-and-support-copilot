import numpy as np
from dataframes import pd, customers_df


def clean_customers(customers_df, ret=True):
    """ Standardizing city values """
    customers_df["city"] = customers_df["city"].str.strip().str.lower()

    """ Standardizing gender values """
    customers_df["gender"] = customers_df["gender"].str.strip().str.lower().map({
        "m": "male",
        "male": "male",
        "f": "female",
        "female": "female"
    })
    customers_df["gender"] = customers_df["gender"].fillna("unknown")


    """ Standardizing age values """
    customers_df.loc[(customers_df["age"] < 10) | (customers_df["age"] > 100), "age"] = np.nan
    customers_df['age'] = customers_df['age'].fillna(customers_df.groupby('city')['age'].transform('median'))

    """ Convert datestring to date """
    customers_df["signup_date"] = pd.to_datetime(customers_df["signup_date"])
    
    if ret:
        return customers_df


clean_customers(customers_df, ret=False)

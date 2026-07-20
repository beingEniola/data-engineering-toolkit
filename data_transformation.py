import pandas as pd

def transform_data(df):
    # Create a new column
    df["total"] = df["price"] * df["quantity"]

    return df

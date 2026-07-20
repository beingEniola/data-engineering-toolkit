import pandas as pd

def clean_data(df):
    # Remove duplicates
    df = df.drop_duplicates()

    # Fill missing values
    df = df.fillna("Unknown")

    #standardize column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    return df
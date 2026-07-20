import pandas as pd

def load_data(df, filename):
    # Save dataframe to CSV
    df.to_csv(filename, index=False)

    print("Data saved successfully")
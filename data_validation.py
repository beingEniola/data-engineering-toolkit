import pandas as pd

def validate_data(input_file, output_file):
    
    # Load data
    df = pd.read_csv(input_file)

    # Remove rows with missing customer IDs
    df = df.dropna(subset=["customer_id"])

    # Keep only valid orders
    df = df[df["quantity"] > 0]
    df = df[df["price"] >= 0]

    # Save validated data
    df.to_csv(output_file, index=False)

    print("Data validation completed successfully.")
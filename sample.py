import pandas as pd
import numpy as np

# Define the number of rows and columns
num_rows = 100
num_cols = 10

# Generate random data
data = np.random.rand(num_rows, num_cols)

# Create a DataFrame with the random data
df = pd.DataFrame(data, columns=[f'column_{i}' for i in range(num_cols)])

# Save the DataFrame to a Parquet file
df.to_parquet('/workspaces/functions-from-zero/data/transactions.parquet')
print("Parquet file has been created successfully.")
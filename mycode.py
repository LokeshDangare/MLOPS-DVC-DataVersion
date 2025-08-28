import pandas as pd
import os

data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

#Adding new row to the DataFrame
new_row = {'name': 'David', 'age': 28, 'city': 'San Francisco'}
df.loc[len(df.index)] = new_row

#Ensure the "data" directory exists at the root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

#Define the file path
file_path = os.path.join(data_dir, 'sample_data.csv')

# Save the DataFrame to a CSV file, including column names
df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")
import os
import pandas as pd

# Get a list of all Excel files in the current directory
excel_files = [file for file in os.listdir() if file.endswith('.xlsx')]

# Initialize an empty list to store DataFrames
dfs = []

# Iterate through each Excel file and read it into a DataFrame
for file in excel_files:
    dfs.append(pd.read_excel(file))

# Concatenate all DataFrames in the list into one DataFrame
merged_df = pd.concat(dfs, ignore_index=True)

# Save the merged DataFrame to a new Excel file
merged_df.to_excel('merged_output.xlsx', index=False)

print("All Excel files have been merged successfully!")

import pandas as pd
import os
import re

# Directory containing the files
directory = 'files/names'

data_frames = []

# Iterate over each file in the directory
for filename in os.listdir(directory):
  if filename.lower().endswith('.txt'):
    file_path = os.path.join(directory, filename)

    # Extract the year from the filename
    match = re.search(r'\d{4}', filename)
    if match:
      year = match.group(0)

    # Read the file into a DataFrame with specified column names
    df = pd.read_csv(file_path, delimiter=',', names=['name', 'gender', 'count'])
    
    # Add the year as a new column
    df['year'] = year

    data_frames.append(df)

# Concatenate all data frames into a single data frame
combined_df = pd.concat(data_frames, ignore_index=True)

# Save the combined data frame as a CSV file
combined_df.to_csv('combined_data.csv', index=False)
import pandas as pd
import os

# Directory containing the files
directory = 'files/namesbystate'

data_frames = []

# Iterate over each file in the directory
for filename in os.listdir(directory):
  if filename.lower().endswith('.txt'):
    file_path = os.path.join(directory, filename)

    # Read the file into a DataFrame with specified column names
    df = pd.read_csv(file_path, delimiter=',', names=['state', 'gender', 'year', 'name', 'count'])

    data_frames.append(df)

# Concatenate all data frames into a single data frame
combined_df = pd.concat(data_frames, ignore_index=True)

# Save the combined data frame as a CSV file
combined_df.to_csv('combined_data_states.csv', index=False)
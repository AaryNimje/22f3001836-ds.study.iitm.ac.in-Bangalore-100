import pandas as pd

# Load the data from repositories.csv
repos_df = pd.read_csv('repositories.csv')

# Step 2: Inspect the data
print(repos_df.head())  # Print first few rows to understand the structure
print("Unique values in 'has_projects':", repos_df['has_projects'].unique())
print("Unique values in 'has_wiki':", repos_df['has_wiki'].unique())

# Step 3: Convert boolean values to integers for correlation
# Ensure that 'has_projects' and 'has_wiki' are treated as numeric (1 for True, 0 for False)
repos_df['has_projects'] = repos_df['has_projects'].replace({True: 1, False: 0}).astype(int)
repos_df['has_wiki'] = repos_df['has_wiki'].replace({True: 1, False: 0}).astype(int)

# Step 4: Drop rows with missing values in either column
repos_df.dropna(subset=['has_projects', 'has_wiki'], inplace=True)

# Step 5: Calculate the correlation
correlation = repos_df['has_projects'].corr(repos_df['has_wiki'])

# Print the result rounded to 3 decimal places
print(f"Correlation between projects and wiki enabled: {correlation:.3f}")

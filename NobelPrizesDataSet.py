import pandas as pd
import numpy as np

# Load the dataset
nobel = pd.read_csv("/Users/jahnavimandadi/Desktop/ExploratoryDataAnalysisOfNobelPrizesProject/archive (1)/complete.csv")

# Preview the top 5 rows of the dataset
print(nobel.head())  # Shows the first 5 rows
print('-' * 75)

# Summarize column information
print(nobel.info())  # Shows information about each column (data types, non-null counts, etc.)
print('-' * 75)

# Generate descriptive statistics
print(nobel.describe())  # Shows summary statistics for numerical columns
print('-' * 75)

# Identify missing values per column
print(nobel.isnull().sum())  # Shows the count of missing values per column

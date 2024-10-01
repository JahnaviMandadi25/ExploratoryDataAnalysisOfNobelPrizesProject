import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
nobel = pd.read_csv("/Users/jahnavimandadi/Desktop/ExploratoryDataAnalysisOfNobelPrizesProject/archive (1)/complete.csv")

# Extract the number of Nobel Prizes per country (y) and country names (x)
y = nobel["birth_country"].value_counts().head(10)
x = y.index

# Plot the data
plt.figure(figsize=(10, 5))
plt.bar(x, y)
plt.xticks(rotation=-45)
plt.ylabel("Number of Nobel Prizes")
plt.title("Top 10 Countries by Number of Nobel Prizes")
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
nobel = pd.read_csv("/Users/jahnavimandadi/Desktop/ExploratoryDataAnalysisOfNobelPrizesProject/archive (1)/complete.csv")

# Create a column to identify laureates hailing from the USA
nobel["born_in_USA"] = nobel["birth_country"] == "USA"

# Determine the annual proportion of US laureates
prop_usa_winners = nobel.groupby("awardYear", as_index=False)["born_in_USA"].mean()

# Create a regression plot
plt.figure(figsize=(10, 5))
sns.regplot(data=prop_usa_winners, x="awardYear", y="born_in_USA")
plt.ylabel("% of USA winners (1.0 equals 100%)")
plt.title("Proportion of Nobel Laureates from the USA Over the Years")
plt.show()


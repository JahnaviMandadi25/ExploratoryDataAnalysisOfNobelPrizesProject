import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
nobel = pd.read_csv("/Users/jahnavimandadi/Desktop/ExploratoryDataAnalysisOfNobelPrizesProject/archive (1)/complete.csv")

# Create a new column to identify if the laureate is female
nobel["female_winner"] = nobel["gender"].str.lower() == "female"

# Calculate the decade for each Nobel Prize award
nobel["decade"] = nobel["awardYear"] // 10 * 10

# Compute the proportion of female winners for each decade and category
prop_female_winners = nobel.groupby(["decade", "category"], as_index=False)["female_winner"].mean()

# Plot the proportion of female winners per decade by categories
plt.figure(figsize=(10, 5))
sns.barplot(x="decade", y="female_winner", hue="category", data=prop_female_winners)
plt.title("The Proportion of Female Winners per Decade by Categories")
plt.ylabel("Female Winners Ratio")
plt.xlabel("Decade")
plt.legend(loc="upper left")
plt.show()

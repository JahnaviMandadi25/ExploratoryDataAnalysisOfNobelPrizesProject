import pandas as pd

# Load the Nobel Prize data
nobel = pd.read_csv("/Users/jahnavimandadi/Desktop/ExploratoryDataAnalysisOfNobelPrizesProject/archive (1)/complete.csv")  # Update this path

# Print the earliest female Nobel Prize recipient
print('The earliest female Nobel Prize recipient:')
earliest_female = nobel[nobel["gender"] == "Female"].nsmallest(1, columns="awardYear")
print(earliest_female)

# Print the earliest male Nobel Prize recipient
print('The earliest male Nobel Prize recipient:')
earliest_male = nobel[nobel["gender"] == "Male"].nsmallest(1, columns="awardYear")
print(earliest_male)

# Print the laureate awarded the largest Nobel Prize amount
print('Laureate awarded the largest Nobel Prize amount:')
largest_prize = nobel.iloc[nobel[["prizeAmount"]].idxmax()]
print(largest_prize)

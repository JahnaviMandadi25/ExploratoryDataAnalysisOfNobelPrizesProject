import nltk
from nltk.corpus import stopwords
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
nltk.download('stopwords')

# Load the dataset
nobel = pd.read_csv("/Users/jahnavimandadi/Desktop/ExploratoryDataAnalysisOfNobelPrizesProject/archive (1)/complete.csv")

# Initialize the 'Filtered motivation' column with empty strings
nobel["Filtered motivation"] = ""

# Apply a lambda function to remove stopwords from the 'motivation' column
nobel["Filtered motivation"] = nobel["motivation"].apply(
    lambda x: " ".join(word for word in str(x).split() if word.lower() not in stopwords.words("english")) if pd.notnull(x) else ""
)

# Concatenate all entries in 'Filtered motivation' to form a single text string
text = " ".join(nobel["Filtered motivation"])

# Split the text into words and create a pandas DataFrame from the list of words
words_df = pd.DataFrame(text.split(), columns=['word'])

# Calculate word frequency
word_freq = words_df['word'].value_counts().reset_index()
word_freq.columns = ['word', 'freq']

# Plotting the 20 most common words using seaborn's barplot
plt.figure(figsize=(10, 8))
sns.barplot(x='freq', y='word', data=word_freq.head(20), palette='viridis')
plt.title('Top 20 Most Common Words in Nobel Prize Motivation')
plt.xlabel('Frequency')
plt.ylabel('Word')
plt.show()

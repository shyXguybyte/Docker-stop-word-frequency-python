import nltk
from nltk.corpus import stopwords
from collections import Counter

# Download NLTK stopwords if not already downloaded
nltk.download('stopwords')

# Function to remove stopwords from text
def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = nltk.word_tokenize(text)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return filtered_words

# Function to count word frequency
def count_word_frequency(words):
    word_count = Counter(words)
    return word_count

# Read contents of the file
file_path = "random_paragraphs.txt"
with open(file_path, 'r') as file:
    text = file.read()

# Remove stopwords
filtered_text = remove_stopwords(text)

# Count word frequency
word_frequency = count_word_frequency(filtered_text)

# Display word frequency count
for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")

import re

# Read the text file
with open('C:/Users/Daveee/Desktop/CBE_project/doc.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Count occurrences of the word 'Cheshire'
# Using \b to match whole words and avoid partial matches
word_count = len(re.findall(r'\bCheshire\b', text))

print(word_count)

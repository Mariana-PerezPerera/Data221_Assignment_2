#iporting string and counter for later use:
import string
from collections import Counter

#opening and reading the text file:
with open("sample-file.txt", 'r') as file:
    text = file.read()

#now we will the text into tokens with 'split':
tokens = text.split()

#now we have to "clean" the tokens and convert them into lower case:
#create an empty list for the cleaned tokens first:
cleaned_tokens = []
for token in tokens:
    #this will convert them into lowercase, using 'lower'
    token = token.lower()
    #remove the punctuation from the beginning as well as the end by using 'strip' and 'string.punctuation':
    token = token.strip(string.punctuation)
    #make sure to keep the tokens with at least two alphabetic characters by using 'sum', 'char.isaplha' and a for loop:
    tokens_with_two_alphabetic_characters = sum(char.isalpha() for char in token)
    #append the tokens that are larger than 2 characters to the cleaned token lost:
    if tokens_with_two_alphabetic_characters >= 2:
        cleaned_tokens.append(token)

#now we have to count the word frequencies, using the counter we imported:
word_frequencies = Counter(cleaned_tokens)

#then print the 10 most frequent words:
for word, count in word_frequencies.most_common(10):
    print(f"{word} -> {count}")

file.close()


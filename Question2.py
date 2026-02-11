import string
from collections import Counter

#open and read the text file:
with open ("sample-file.txt", "r") as file:
    text = file.read()

#spitting it up into tokens:
tokens = text.split()

#convert the tokens into lowercase:
cleaned_tokens = []
for token in tokens:
    #conert all the tokens into lower case:
    token = token.lower()
    #remove the punctuation from the beginning and end of each token:
    token = token.strip(string.punctuation)
    #finding the tokens with only 2 alphabetic letters and keeping them:
    tokens_with_two_alphabetic_characters = sum(char.isalpha() for char in token)
    #appending/keeping the tokens that contain at least 2 alphabetic characters:
    if tokens_with_two_alphabetic_characters >= 2:
        cleaned_tokens.append(token)

#count the frequency of each bigram:
#first create an empty list for the bigrams:
bigrams = []

#use a for loop to store them as a tuple so we can then count them:
for i in range(len(cleaned_tokens)- 1):
    bigram = cleaned_tokens[i], cleaned_tokens[i+1]
    bigrams.append(bigram)

#now we can count the bigram frequencies:
bigram_frequency = Counter(bigrams)

#print the 5 most frequent bigrams:
for (word1, word2), count in bigram_frequency.most_common(5):
    print(f"{word1} {word2} -> {count}")



import spacy as spacy
from nltk.corpus import gutenberg
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import csv
from nltk import pos_tag
from collections import Counter
import re

stop_words = set(stopwords.words('english'))
emma = gutenberg.raw('austen-emma.txt')

# Tokenizing corpus
tok = word_tokenize(emma)

# Removing non-alphabeticc char
newOutput = [word for word in tok if word.isalpha()]
print(newOutput)

# Removing Stop words from corpus
filtered_sentence = []
for w in newOutput:
    if w not in stop_words:
        filtered_sentence.append(w)

# Performing Freq Distribution on corpus
fd = FreqDist(filtered_sentence)

# 50 most frequent tokens
print(fd.most_common(50))

# Applying POS Tags
taggedOutput = pos_tag(filtered_sentence)
print(taggedOutput)

# Exporting vocabulary of the book to csv

with open('Assignment1_Part1_Token_Fre_Distribution.csv', 'w',
          newline='') as csvfile:
    fieldNames = ['Token', 'Frequency (in %)']
    writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
    writer.writeheader()
for key,value in fd.items():
    value = (value/fd.N())*100
    #print(key,value)
    with open('Assignment1_Part1_Token_Fre_Distribution.csv', 'a',
              newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
        writer.writerow({'Token': key, 'Frequency (in %)': value})

# Finding Freq Dist of POS Tags
tagDict = {}
for key,value in taggedOutput:
    #print(key,value)
    if value in tagDict.keys():
        counter = tagDict.get(value)
        counter = counter+1
        tagDict[value] = counter
    else:
        tagDict[value] = 0

# Top 50 POS Tags are -
print(sorted(tagDict.items(), key=lambda x: x[1], reverse=True)[:50])

# Find Person name in corpus
nlp = spacy.load('en_core_web_sm')
doc = nlp(emma)
person= {}
for ent in doc.ents:
    if ent.label_ == "PERSON":
        if ent.text in person.keys():
            oldcounter = person[ent.text]
            counter = oldcounter+1
            person[ent.text] = counter
        else:
            person[ent.text] = 1

#Sorting dictionary to find top 20 names

print(sorted(person.items(), key=lambda x: x[1], reverse=True)[:20])

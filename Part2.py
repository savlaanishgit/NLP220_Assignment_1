from nltk.corpus import reuters
from nltk.probability import FreqDist
import csv
import matplotlib.pyplot as plt
import pandas as pd

fd1 = FreqDist(reuters.categories())
print(fd1.items())
# Frequency Distribution of Words
fd = FreqDist(reuters.words())

# Top 10 words according to Frequency
top_10_fd = fd.most_common(10)
print(top_10_fd)

# Normalizing Values for Freq dist

for key,value in fd.items():
    value = value / fd.N()
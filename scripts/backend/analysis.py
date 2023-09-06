#!/usr/bin/env python
import numpy as np
import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

output_file = './data/output/matrix.txt'

nephi_file = open("./data/text/nephi.txt", "r")
nephi_data = nephi_file.read().split("$")
nephi_file.close()

alma_file = open("./data/text/alma.txt", "r")
alma_data= alma_file.read().split("$")
alma_file.close()

data = nephi_data.copy()
data.extend(alma_data)

#Lemmitization converts words to useful base form
lemmer = nltk.stem.WordNetLemmatizer()
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

Vectorizer = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')

def cos_similarity(textlist):
    tfidf = Vectorizer.fit_transform(textlist)
    return (tfidf * tfidf.T).toarray()

m = cos_similarity(data)

# mat = np.matrix(m)

# with open(output_file,'wb') as f:
#     for line in mat:
#         np.savetxt(f, line, fmt='%.2f')

# exit()

print("Enter a chapter in 1 Nephi:")
targetChapter = input()
# targetChapter = np.floor(input())
# if(targetChapter < 1 | targetChapter > 22):
#     print("Chapter does not exist. Please try again:")
#     targetChapter = np.floor(input())

print("Enter a verse")
targetVerse = input()

target = [i for i, s in enumerate(nephi_data) if (str(targetChapter) + ":" + str(targetVerse)) in s][0]

#print(target)

offset = len(nephi_data)
nephiMat = m[target,offset:]
position = np.unravel_index(np.argmax(nephiMat, axis=None), nephiMat.shape)[0]

print("\nTarget:\n1 Nephi " + nephi_data[target])
print("Result:\nAlma " + alma_data[position])
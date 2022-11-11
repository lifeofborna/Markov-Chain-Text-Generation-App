#!/usr/bin/env python
import os
import nltk
import re

def read_from_file():
    words = []
    dirname = os.path.dirname(__file__)
    data_file_path = os.path.join(dirname, "got1.txt")

    with open(data_file_path) as f:
        for line in f:
            line = line.strip()
            if line != "":
                words.append(line)

    cleaned_words = clean_text_file(words)

    print(cleaned_words)
    return cleaned_words


def clean_text_file(text):
    nltk.download('punkt')
    processed_text = []
    #TODO lower all words --> remove all punctuations --> tokenize make states
    for row in text:
        row = row.lower()
        row = re.sub(r'[^\w\s]','',row)
        states = nltk.word_tokenize(row)
        words = [word for word in states if word.isalpha()]
        processed_text+=words
    return processed_text

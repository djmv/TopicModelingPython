# -*- coding: utf-8 -*-
"""
Created on Sun Feb 04 22:03:17 2018

@author: Mendez Vasquez
Load a text file from folder texts and make a topic modeling of txt file.
You can add more txt files to folder texts and do a topic modeling for those files. 
"""
import os
import numpy as np  # a conventional alias
import sklearn.feature_extraction.text as text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
import unicodedata
import codecs

def load_codecs(file_name):
	with codecs.open(file_name, "r",encoding='latin_1', errors='ignore') as fdata:
		return fdata.readlines()

def elimina_tildes(s):
   s = ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
   return s.decode()

def load_file(filename):
    with open(filename, 'r') as myfile:
        data=myfile.read().replace('\n', '')
    return data

def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print ("Topic %d:" % (topic_idx))
        print (" ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]]))
    
CORPUS_PATH = os.path.join('texts')

translator = Translator()
filenames = sorted([os.path.join(CORPUS_PATH, fn) for fn in os.listdir(CORPUS_PATH)])
print(filenames)
texto = [load_codecs(txt_file) for txt_file in filenames]
texto = texto[0] #take 1 first text


tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2,stop_words='english')
tfidf = tfidf_vectorizer.fit_transform(texto)
tfidf_feature_names = tfidf_vectorizer.get_feature_names()

no_topics = 5 #Number of topics
nmf = NMF(n_components=no_topics, random_state=1, alpha=.1, l1_ratio=.5, init='nndsvd').fit(tfidf)

no_top_words = 10
display_topics(nmf, tfidf_feature_names, no_top_words)
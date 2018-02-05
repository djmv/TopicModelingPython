# -*- coding: utf-8 -*-
"""
Created on Sun Feb 04 22:03:17 2018

@author: Mendez Vasquez
"""
import os
import numpy as np  # a conventional alias
import sklearn.feature_extraction.text as text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
#from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import unicodedata

def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

def load_file(filename):
    with open(filename, 'r') as myfile:
        data=myfile.read().replace('\n', '')
    return data

def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print "Topic %d:" % (topic_idx)
        print " ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]])
    
CORPUS_PATH = os.path.join('texto')

filenames = sorted([os.path.join(CORPUS_PATH, fn) for fn in os.listdir(CORPUS_PATH)])

texto = [load_file(txt_file) for txt_file in filenames]

textodecode = [textodec.decode('utf-8', 'replace') for textodec in texto]

textodecode2 = [textodec.decode('utf8') for textodec in texto]

tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2)
tfidf = tfidf_vectorizer.fit_transform(textodecode)
tfidf_feature_names = tfidf_vectorizer.get_feature_names()

no_topics = 5
nmf = NMF(n_components=no_topics, random_state=1, alpha=.1, l1_ratio=.5, init='nndsvd').fit(tfidf)

no_top_words = 10
display_topics(nmf, tfidf_feature_names, no_top_words)

"""
vectorizer = text.CountVectorizer(input='filename', min_df=20)
dtm = vectorizer.fit_transform(filenames).toarray()
vocab = np.array(vectorizer.get_feature_names())
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 11:20:12 2018

@author: Mendez Vasquez
"""

import psycopg2
import os
import numpy as np  # a conventional alias
import sklearn.feature_extraction.text as text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
import unicodedata
import codecs
from googletrans import Translator

def load_codecs(file_name):
	with codecs.open(file_name, "r",encoding='latin_1', errors='ignore') as fdata:
		return fdata.readlines()

CORPUS_PATH = os.path.join('texto')

translator = Translator()
filenames = sorted([os.path.join(CORPUS_PATH, fn) for fn in os.listdir(CORPUS_PATH)])

texto = [load_codecs(txt_file) for txt_file in filenames]
texto = texto[0]

try:
    conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='1234'")
except:
    print "I am unable to connect to the database"
    
cur = conn.cursor()
#cur.execute("CREATE TABLE publicaciones (id serial PRIMARY KEY, grupo varchar, publicacion varchar);")
#for item in texto:
#    cur.execute("INSERT INTO publicaciones (grupo, publicacion) VALUES (%s, %s)",("Kopi",item))

cur.execute("SELECT publicacion FROM publicaciones;")
while cur.fetchone():
    print cur.fetchone()
conn.commit()
cur.close()
conn.close()
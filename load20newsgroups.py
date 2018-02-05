# -*- coding: utf-8 -*-
"""
Created on Sun Feb 04 13:25:11 2018

@author: Mendez Vasquez
"""
from sklearn.datasets import fetch_20newsgroups

dataset = fetch_20newsgroups(shuffle=True, random_state=1, remove=('headers', 'footers', 'quotes'))
documents = dataset.data
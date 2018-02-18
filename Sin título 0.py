# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 11:20:12 2018

@author: Mendez Vasquez
"""

import psycopg2

try:
    conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='1234'")
except:
    print "I am unable to connect to the database"
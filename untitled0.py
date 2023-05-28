# -*- coding: utf-8 -*-
"""
Created on 07 May 2023

@developer: Khushi Sharma
"""


import csv
import pandas as pd
import random
New=[]
with open('movieR.csv','r') as csvfile:
    readCSV = csv.reader(csvfile)
    New.append(random.choice(list(readCSV)))
print(New[0][0])
        
        
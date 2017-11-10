# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 18:31:59 2017

@author: Mrigakshi
"""
import re


file=open('a.txt','r+')
mystr = file.read()
wordList = re.sub("[^\w]", " ",  mystr).split()
file.close()
wordList[0]='11'
myster=' '.join(wordList)
file=open('a.txt','w+')
file.write(myster)
file.close()
file=open('a.txt','r+')
mystr = file.read()
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 21:35:22 2022

@author: Dark lord
"""

class analysed(object):
    def __init__(self,text):
        fmtxt = text.replace(","," ").replace(","," ").replace("!"," ").replace(" "," ").replace("?", " ")
        fmtxt = fmtxt.lower()
        self.text = fmtxt
        
    def freqall(self):
        wordlist=self.text.split(" ")
        freqmap={}
        for i in set(wordlist):
            freqmap[i]=wordlist.count(i)
        
        return freqmap
    
    def freqof(self,word):
        freqdict=self.freqall()
        
        if word in freqdict:
            return freqdict[word]
        else:
            print("Not there")

q=open("E:/SQL/External Video-en.txt","r",encoding="utf8")
x=q.read()
#print(x)
#samplePassage=[]
samplePassage = analysed(x)

print(samplePassage.freqall())
search=input("Enter the word you want to check : ")
print(samplePassage.freqof(search))
q.close()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 12:43:37 2018

@author: juancastro
"""

"""
from gtts import gTTS
tts = gTTS('hello USCO 2018', lang="es")
tts.save('hello.mp3')
"""
"""
from pymongo import MongoClient
client = MongoClient()
db = client['greeting']
collection = db['saludo']
data = collection.find_one({"language": "fr"})
print(type(data))
print(data)

GM = data["GM"]
GA = data["GA"]
GE = data["GE"]

print(GM)
print(GA)
print(GE)
"""
from pyknow import *

class Greeting(Fact):
    pass

class Saludar(KnowledgeEngine):
    greeting = ""
    
    def setGreeting(self, g):
        self.greeting = g
    
    def getGreeting(self):
        return self.greeting
        
    def getMessage(self):
        return self.getGreeting()
    

    @Rule(Greeting(hora = P(lambda hora: hora >= 0) & P(lambda hora: hora <= 11)))
    def morning(self):
        self.setGreeting("GM")

    @Rule(Greeting(hora = P(lambda hora: hora >= 12) & P(lambda hora: hora <= 17)))
    def afternoon(self):
        self.setGreeting("GA")
        
    @Rule(Greeting(hora = P(lambda hora: hora >= 18) & P(lambda hora: hora <= 23)))
    def evening(self):
        self.setGreeting("GE")


watch('RULES', 'FACTS')
nxm = Saludar()  
nxm.reset()

#        language = "en"
hora = 20

nxm.declare(Greeting(hora=hora))
nxm.run()
nxm.facts      
        
greeting = nxm.getMessage()
print(greeting)
        
        










# Implementation of pset5 dictionary.c in Python

words = dict()

def check(word):
    if word in words:
        return True
    else:
        return False

def load(dictionary):
file = open(dictionary, "r")
for line in file:
    
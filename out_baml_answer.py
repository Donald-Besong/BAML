import re
import pandas as pd
import numpy as np
import math


#*****************begin reading arguments
import pathlib
p = pathlib.Path(__file__).parent.resolve()
data_source = p.joinpath("words.txt")
words = open(data_source).readlines()
words = [line[:-1] for line in words]

#print(words)
# Given a words.txt file containing a newline-delimited list of dictionary
# words, please implement the Anagrams class so that the get_anagrams() method
# returns all anagrams from words.txt for a given word.
#
# Requirements:
#   - Optimise the code for fast retrieval
#   - Write more tests
#   - Thread safe implementation

import unittest
def sort_list(mylist):
    def fun(z):
            return z.lower()
    mylist.sort(key=fun)
    return mylist
    
class Anagrams:

    def __init__(self):
        self.words = words

    def get_anagrams(self, word):
        word = "".join(sorted(word,key=lambda x:x.lower()))
        word_list = ["".join(sorted(a,key=lambda x:x.lower())) for a in self.words]
        anagrams = [xtest for xtest in self.words if "".join(sorted(xtest,key=lambda x:x.lower()))==word]
        anagrams = sort_list(anagrams)
        return anagrams


class TestAnagrams(unittest.TestCase):

    def test_anagrams(self):
        anagrams = Anagrams()
        self.assertEquals(anagrams.get_anagrams('plates'), sort_list(['palest', 'pastel', 'petals', 'plates', 'staple', 'pleats']))
        self.assertEquals(anagrams.get_anagrams('eat'), sort_list(['ate', 'eat', 'tea', 'eta']))


if __name__ == '__main__':
    unittest.main() #comment out this and uncomment the below two lines to try other anagrams
    #my_object = Anagrams()
    #my_object.get_anagrams("bade")

out_all = ["arbitrary0","arbitrary1", "arbitrary2", "arbitrary3"]



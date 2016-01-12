from collections import Counter
import re

from resource import greek_untranslatables 

def try_with_zipfs_law():
  ''' Use Zipf's Law to identify words with the same counts'''
  #use counter for greek and latin text



def greek_text_rip():
    """ 
    Function for initial preparation of the Greek texts from Musaios
    """
    pass


def latin_text_rip():
    """
    Function for initial preparation of the Latin texts from Musaios
    """
    pass



def read_verses(latin_text):
    """
    For latin vulgate: read verses
    """
    lines = open(latin_text).read().split('\n')
    for line in lines:
        chapter_and_verse = line.split(' ')[0]
        chapter, verse = chapter_and_verse.split()[0], chapter_and_verse.split()[1]
    return

def clean_clementina(text):
    """
    Clean the text of clementina
    """
    to_be_replaced = {"æ":"ae","œ":"oe", "Æ": "AE" } #"ë":"?"
    for key in to_be_replaced.keys():
        text.replace(key, to_be_replaced[key])


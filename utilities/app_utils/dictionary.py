# dictionary function
from PyDictionary import PyDictionary

"""
Please add a sample request and response in the docstrings
Check out with prashant I have explained him about this
"""

def dictionary_result(term):
    """
	Takes an input string and returns a dictionary with
	the orignal term, meaning, synonym and antonyms
	"""
    dictionary = PyDictionary()  # creating instance of the PyDictionary
    return_data = {}
    # dictionary keys
    return_data['term'] = term
    return_data['term_meaning'] = dictionary.meaning(term) # returns the meaning of the term
    return_data['term_synonym'] = dictionary.synonym(term) # returns the synonyms of the term
    return_data['term_antonym'] = dictionary.antonym(term) # returns the antonyms of the term
    return return_data

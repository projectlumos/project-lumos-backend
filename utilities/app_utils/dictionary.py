# dictionary function
from PyDictionary import PyDictionary


def dictionary_result(term):
    """
	Takes an input string and returns a dictionary with
	the orignal term, meaning, synonym and antonyms
    request : https://pl-backend-staging.herokuapp.com/dict/compress/
    response :
    {
    "term": "compress",
    "term_meaning": {
        "Noun": [
            "a cloth pad or dressing (with or without medication",
            "to relieve discomfort or reduce fever"
        ],
        "Verb": [
            "make more compact by or as if by pressing",
            "squeeze or press together"
        ]
    },
    "term_synonym": [
        "abbreviate",
        "shorten",
        "restrict",
        "wrap",
        "cram"
        ],
        "term_antonym": [
        "amplify",
        "enlarge",
        "increase",
        "lengthen",
        "grow"
        ]
    }
	"""
    # creating instance of the PyDictionary
    dictionary = PyDictionary()
    return_data = {}

    # dictionary keys
    return_data['term'] = term

    # returns the meaning of the term
    return_data['term_meaning'] = dictionary.meaning(term)

    # returns the synonyms of the term
    return_data['term_synonym'] = dictionary.synonym(term)

    # returns the antonyms of the term
    return_data['term_antonym'] = dictionary.antonym(term)
    return return_data

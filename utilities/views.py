from django.shortcuts import render
from django.http import HttpResponse

# framework level libraries
from rest_framework.decorators import api_view
from rest_framework.response import Response

# external imports
import wikipedia
from PyDictionary import PyDictionary

# app level imports
from utilities.app_utils import wiki, dictionary

# Create your views here.

@api_view(['GET'])
def wikiscript(request, term):
    """
    This is a function that takes in request and a term from url
    which is a slug and runs wikipedia functions to return JSON data
    request : http://127.0.0.1:8000/wiki/ruby-language/
    response :
    {
            "wiki_term": "ruby-language",
            "detailed_data": {
            "title": "Ruby (programming language)",
            "url": "https://en.wikipedia.org/wiki/Ruby_(programming_language)",
            "content": "Ruby is a dynamic, reflective, object-oriented,
            general-purpose programming language. It was designed and developed
            "
            },
            "summary_data": {
            "summary_present": true,
            "summary_content": "Ruby is a dynamic, reflective, object-oriented, general-purpose programming language"
            },
            "related_terms": {
            "Ruby (programming language)": "https://en.wikipedia.org/wiki/ruby_(programming_language)",
            "Ruby": "https://en.wikipedia.org/wiki/ruby",
            "Ruby MRI": "https://en.wikipedia.org/wiki/ruby_mri",
            "Ruby on Rails": "https://en.wikipedia.org/wiki/ruby_on_rails",
            "Ruby character": "https://en.wikipedia.org/wiki/ruby_character"
            }
    }
    """
    term = str(term)
    # passing the term from url to get_wiki_product_data
    wiki_dict = wiki.get_wiki_product_data(term)
    return Response(wiki_dict)

@api_view(['GET'])
def dictscript(request, term):
    """
    This is a function that takes in request and a term from url
    which is a slug and runs dictionary function to return JSON data
    request : http://127.0.0.1:8000/dict/compress/
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
    term = str(term)
    # passing the term from url to dictionary_result
    dict_dict = dictionary.dictionary_result(term)
    return Response(dict_dict)

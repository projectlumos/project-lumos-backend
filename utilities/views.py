from django.shortcuts import render
from django.http import HttpResponse
import wikipedia
from PyDictionary import PyDictionary
from utilities.app_utils import wiki, dictionary
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def wikiscript(request, term):
    """
    This is a function that takes in request and a term from url
    which is a slug and runs wikipedia functions to return JSON data
    """
    term = str(term)
    wiki_dict = wiki.get_wiki_product_data(term)  #passing the term from url to get_wiki_product_data
    return Response(wiki_dict)

@api_view(['GET'])
def dictscript(request, term):
    """
    This is a function that takes in request and a term from url
    which is a slug and runs dictionary function to return JSON data
    """
    term = str(term)
    dict_dict = dictionary.dictionary_result(term)  #passing the term from url to dictionary_result
    return Response(dict_dict)

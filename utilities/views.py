from django.shortcuts import render
from django.http import HttpResponse
import wikipedia
from PyDictionary import PyDictionary
import json
from django.http import JsonResponse
# Create your views here.

#wikipedia functions
def wiki_term_to_url(terms_list):
    """
    takes a term list and returns a dict
    which contains the term and the wikipedia url
    """
    wiki_data = {curr_term: 'https://en.wikipedia.org/wiki/' + curr_term.lower().replace(' ','_') for curr_term in terms_list}  #for every term in the list, concatenate with default wiki_url, make it lowercase and replace space with _ for url purposes
    return wiki_data

def get_wiki_data(term):
    """
    Input: term, a string
    Output: return_data, a dictionary
    Returns page title, page url, page content for term
    Returns False if it encounters a ConnectionError
    """
    return_data = {}
    try:
        term_data = wikipedia.page(term)
        return_data['title'] = term_data.title
        return_data['url'] = term_data.url
        return_data['content'] = term_data.content
    except Exception as e:
        print(e)  #if exception is thrown, print it
        return_data = None
    return return_data  #if no exception return title, url and content of the term in dictionary

def get_similar_search(term, results = 5):
    """
    Input: term, a string, results limited to 5
    Output: return_data, a dict
    Returns a dict containing related term asa key and the wiki url as valuege
    Returns False if it encounters a ConnectionError
    """
    return_data = None
    try:
        all_terms = wikipedia.search(term, results=results)  #search the related terms and limit to results specified
        return_data = wiki_term_to_url(all_terms)  #pass the all_terms list into wiki_term_to_url to get indivisual urls of each related term
    except Exception as e:
        print(e)  #if exception is thrown, print it
        return_data = None
    return return_data  #dictionary with related terms and thier urls

def get_wiki_summary(term, sentences=4):
    """
    Input: term, a string. sentences, an interger
    Output: string
    Returns the summary for term with a constraint on the number of sentences. Default = 3
    Returns a dict of approx links with their wikipedia urls
    """
    return_data = {}
    try:
        return_data['summary_present'] = True  #if no ambiguation, set summary_present to True
        return_data['summary_content'] = wikipedia.summary(term, sentences)  #find the summary of the term and limit to 4 sentences
    except wikipedia.exceptions.DisambiguationError as e:
        return_data['summary_present'] = False   #ambiguation exists, set summary_present to False
        approx_links = e.options  #e.options give ambiguation results
        return_data['other_links'] =  wiki_term_to_url(approx_links) #get the urls of the ambiguous terms
    return return_data


def get_wiki_product_data(term):
    """
    runs the wikiperdia helper functions and created the
    wikipedia data ready for the modal
    """
    try:
        return_data = False
        detailed_data = get_wiki_data(term=term)  #gets the title, url and content of the term
        summary_data = get_wiki_summary(term=term)  #gets the summary or ambiguous results with urls
        related_terms = get_similar_search(term=term) #gets related terms and urls
        if summary_data:
            return_data = {
                    'wiki_term': term,
                    'detailed_data' : detailed_data,
                    'summary_data': summary_data,
                    'related_terms': related_terms
            }
        return return_data #dictionary with the submitted term, detailed_data, summary_data and related_terms

    except wikipedia.exceptions.PageError as e:
        return_data = None
        return return_data

#dictionary function
def dictionary_result(term):
	"""
	Takes an input string and returns a dictionary with
	the orignal term, meaning, synonym and antonyms
	"""
	dictionary = PyDictionary()  #creating instance of the PyDictionary class
	return_data = {}
	#dictionary keys
	return_data['term'] = term
	return_data['term_meaning'] = dictionary.meaning(term)  #returns the meaning of the term
	return_data['term_synonym'] = dictionary.synonym(term)  #returns the synonyms of the term
	return_data['term_antonym'] = dictionary.antonym(term)  #returns the antonyms of the term
	return return_data


def wikiscript(request, term):
    term = str(term)
    wiki_dict = get_wiki_product_data(term)
    wiki_dict = json.dumps(wiki_dict)
    return JsonResponse(json.loads(wiki_dict))

def dictscript(request, term):
    term = str(term)
    dict_dict = dictionary_result(term)
    dict_dict = json.dumps(dict_dict)
    return JsonResponse(json.loads(dict_dict))

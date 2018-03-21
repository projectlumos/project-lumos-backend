# wikipedia functions
import wikipedia
import logging
logger = logging.getLogger(__name__)
from utilities.constants import WIKI_BASE_URL


def wiki_term_to_url(terms_list):
    """
    takes a term list and returns a dict
    which contains the term and the wikipedia url
    """
    # for every term in the list, concatenate with default wiki_url, make it lowercase and replace space with _ for url purposes
    wiki_data = {curr_term: WIKI_BASE_URL + curr_term.lower().replace(' ','_') for curr_term in terms_list}
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
        logger.error(e)
        return_data = None
    # if no exception return title, url and content of the term in dictionary
    return return_data

def get_similar_search(term, results = 5):
    """
    Input: term, a string, results limited to 5
    Output: return_data, a dict
    Returns a dict containing related term asa key and the wiki url as valuege
    Returns False if it encounters a ConnectionError
    """
    return_data = None
    try:
        # search the related terms and limit to results specified
        all_terms = wikipedia.search(term, results=results)
        # pass the all_terms list into wiki_term_to_url to get indivisual urls of each related term
        return_data = wiki_term_to_url(all_terms)
    except Exception as e:
        logger.error(e)
        return_data = None
    # dictionary with related terms and thier urls
    return return_data

def get_wiki_summary(term, sentences=4):
    """
    Input: term, a string. sentences, an interger
    Output: string
    Returns the summary for term with a constraint on the number of sentences. Default = 3
    Returns a dict of approx links with their wikipedia urls
    """
    return_data = {}
    try:
         # if no ambiguation, set summary_present to True
        return_data['summary_present'] = True
        # find the summary of the term and limit to 4 sentences
        return_data['summary_content'] = wikipedia.summary(term, sentences)
    except wikipedia.exceptions.DisambiguationError as e:
        # ambiguation exists, set summary_present to False
        return_data['summary_present'] = False
        # e.options give ambiguation results
        approx_links = e.options
        # get the urls of the ambiguous terms
        return_data['other_links'] =  wiki_term_to_url(approx_links)
    return return_data


def get_wiki_product_data(term):
    """
    runs the wikiperdia helper functions and created the
    wikipedia data ready for the modal
    """
    return_data = {}
    try:
        # gets the title, url and content of the term
        detailed_data = get_wiki_data(term=term)
        # gets the summary or ambiguous results with urls
        summary_data = get_wiki_summary(term=term)
        # gets related terms and urls
        related_terms = get_similar_search(term=term)
        if summary_data:
            return_data = {
                    'wiki_term': term,
                    'detailed_data': detailed_data,
                    'summary_data': summary_data,
                    'related_terms': related_terms
            }

    except wikipedia.exceptions.PageError as e:
        return_data['error'] = "page doesn't exist or could not be loaded."

    # dictionary with the submitted term, detailed_data, summary_data and related_terms
    return return_data

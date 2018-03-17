import urllib

def create_redirect_url(query_params, base_url):
    """
    Creating a redirect url with data and status encoded 
    :param query_params: dict to be encoded in url as query params
    :param base_url: Base url to be prefixed to the query params
    :return: Base url encoded with the query params
    """

    encoded_params = urllib.urlencode(query_params)
    return '{0}?params={1}'.format(base_url, encoded_params)

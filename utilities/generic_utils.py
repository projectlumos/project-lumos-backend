from urllib.parse import urlencode


def create_query_paramed_url(base_url, payload):
    """
    Encoding a URL with query params provided in a dict
    
    :param base_url: 
    :param payload: 
    :return: 
    """

    encoded_params = urlencode(payload)
    return base_url.format(encoded_params)

import datetime

import pytz


def get_epoch(input_timestamp):
    """
    
    :param input_timestamp: 
    :return: 
    """

    epoch = datetime.datetime.timestamp(input_timestamp)
    return epoch


def get_current_time():

    now = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata'))
    return now


def epoch_in_past(given_epoch):
    """
    
    :param given_epoch: 
    :return: 
    """
    now = get_current_time()
    now_epoch = get_epoch()

    return True if now_epoch >= given_epoch else False


def epoch_in_future(given_epoch):
    """
    
    :param given_epoch: 
    :return: 
    """

    return not epoch_in_past(given_epoch)
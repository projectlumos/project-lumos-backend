from django.core.exceptions import PermissionDenied
from rest_framework_jwt.settings import api_settings

from accounts.models import LumosUser


def get_lumos_user_data(user):
    """
    LumosUser data with key profile information
    :param user: django user object
    :return: dict
    """

    lumos_user_object = LumosUser.objects.filter(id=user.id)

    return_data = {
        'id': user.id,
        'email': user.email,
        'is_verified': user.lumos_user.is_verified
    }

    return return_data


def jwt_response_payload_handler(token=None, user=None, request=None):
    """
    /auth/login/ will redirect to this endpoint
    
    User auth using tokens or user object wrapper around vanilla auth/login
    
    :param token: 
    :param user: 
    :param request: 
    :return: token and lumos_user_data
    """

    if not hasattr(user, 'lumos_user'):
        raise PermissionDenied("Invalid User!")

    lumos_user_data = get_lumos_user_data(user)

    if token is None:
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

    data = {
        'token': token,
        'user': lumos_user_data
    }

    return data

# django imports

# drf imports

# project level

# app level
from accounts.constants import DJANGO_USERNAME_LIMIT


def validate_email(email):
    """
    Using default django functions to validate the email IDs
    
    :param email: string
    :return: bool
    """
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    if not email:
        return False
    else:
        email = email.strip()

    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


def validate_user_creation_params(user_creation_params):
    """
    Used to validation user creation params
    
    :param user_creation_params:
                                    { 
                                        email: email,
                                        password1: password,
                                        password2: password,
                                        first_name: first name,
                                        last_name: last name
                                    }
    
    :return: dict: {status: bool, message: str} 
    """
    response = dict()
    response['status'] = True
    response['message'] = None

    email = user_creation_params.get('email')
    password = user_creation_params.get('password')
    password1 = user_creation_params.get('password1')
    first_name = user_creation_params.get('first_name')
    last_name = user_creation_params.get('last_name')


    # validate email
    email_valid = validate_email(email)

    if not email_valid:
        response['status'] = False
        response['message'] = "Email address has invalid format"

        return response

    # check password fields
    if not password or not password1:
        response['status'] = False
        response['message'] = "Please provide valid password"

        return response

    # passwords should match
    if password != password1:
        response['status'] = False
        response['message'] = "Your passwords do not match"

        return response

    if len(email) >= DJANGO_USERNAME_LIMIT:
        response['status'] = False
        response['message'] = "Your email is too long! Please try again with a shorter email!"

    return response



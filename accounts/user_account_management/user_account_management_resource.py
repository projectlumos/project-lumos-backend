import json

from django.contrib.auth import logout


from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, \
    HTTP_503_SERVICE_UNAVAILABLE
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# project level
from accounts.models import User, LumosUser
from utilities.app_utils.crpyto_utils import lumos_encryption_service
from utilities.datetime_utils import epoch_in_future
from backend.utils import get_lumos_user_data
from utilities.generic_utils import create_query_paramed_url

# app level
from accounts.user_account_management.user_account_management_helper import validate_user_creation_params
from accounts.utils.mailers import send_lumos_user_verification_email
from accounts.constants import HOME_PAGE_URL


@api_view(['POST'])
@permission_classes([AllowAny])
def create_lumos_user(request):
    """
    Endpoint to create LumosUser. Prereq for LumosUser is creating Django User
    Several validity checks are conducted before successful operation.
    
    :param request: 
                     {
                    "email": "darth-dodo@ymaol.com",
                    "password": "apples",
                    "password1": "apples1"
                }
    
    :return:
     400 {"message": "Your email is too long! Please try again with a shorter email!", "status": false}
     400 {"status": false, "message": "Your passwords do not match"}
     400 {"status": false, "message": "You are already Lumos user"}
     
     200
    """

    # base level validations
    request_params = dict()

    response_data = dict()
    response_data['status'] = True

    request_params['email'] = request.data.get('email')
    request_params['password'] = request.data.get('password', None)
    request_params['password1'] = request.data.get('password1', None)

    user_params_valid = validate_user_creation_params(user_creation_params=request_params)

    if not user_params_valid.get('status'):
        return Response(data=user_params_valid, status=HTTP_400_BAD_REQUEST)

    email = request.data.get('email').strip()
    password = request.data.get('password', None).strip()

    # optional params
    first_name = request.data.get('first_name', None).strip() if request.data.get('first_name', None) else None
    last_name = request.data.get('last_name', None).strip() if request.data.get('last_name', None) else None

    email = email.lower()
    django_user, user_created = User.objects.get_or_create(username=email, defaults={'email': email,
                                                                                     'username': email})

    if user_created is True:
        django_user.set_password(password)
        if first_name:
            django_user.first_name = first_name
        if last_name:
            django_user.last_name = last_name
        django_user.save()

        # creating lumos user
        lumos_user = LumosUser()
        lumos_user.id = django_user
        lumos_user.save()
    else:
        # existing Lumos User is trying to access the endpoint
        if hasattr(django_user, 'lumos_user'):
            response_data['status'] = False
            response_data['message'] = "You are already Lumos user"
            return Response(data=response_data, status=HTTP_400_BAD_REQUEST)

    # response_data['id'] = int(django_user.id)

    lumos_user_data = get_lumos_user_data(django_user)

    return Response(data=lumos_user_data, status=HTTP_201_CREATED)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication, BasicAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def logout_lumos_user(request):
    """
    Logs out the request user
    Uses default django code
    
    :param request: 
    :return: 
    """
    logout(request)
    return Response(data="Successfully logged out.", status=HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication, BasicAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def email_verification_request(request):
    """
    User can request the system to send a verification link to validate the user email
    
    :param request: 
    :return: 
    """

    response_data = dict()

    django_user = request.user

    if not hasattr(django_user, 'lumos_user'):
        response_data['status'] = False
        response_data['message'] = "Lumos User not present"
        return Response(data=response_data, status=HTTP_400_BAD_REQUEST)

    else:

        lumos_user = django_user.lumos_user

        if lumos_user.is_verified:
            response_data['status'] = False
            response_data['message'] = "Your email Id is already verified!"
            return Response(data=response_data, status=HTTP_400_BAD_REQUEST)

        email_sent = send_lumos_user_verification_email(lumos_user_obj=django_user.lumos_user)

        if email_sent:
            response_data['status'] = True
            response_data['message'] = "Verification email sent"
            return Response(data=response_data, status=HTTP_200_OK)

        else:
            response_data['status'] = False
            response_data['message'] = "Server error in sending Verification email"
            return Response(data=response_data, status=HTTP_503_SERVICE_UNAVAILABLE)


@api_view(['GET'])
@permission_classes([AllowAny])
def verify_user(request):
    """
    Takes in a tokenized url and checks whether the token is valid and marks the User id embedded with the
    token as verified
    
    Redirects the browser to the home page url with the lumos_user_token which can be exchanged for lumos_user_data
    
    :param request: 
    :return: 
    """

    encrypted_token = request.query_params.get('token', None)

    decrypted_token = lumos_encryption_service(data=encrypted_token.strip(), encrypt_mode=False)

    token_data = json.loads(decrypted_token)

    response_data = dict()

    django_id = token_data.get('id', None)
    epoch = token_data.get('expiry', None)

    if not django_id or not epoch:
        response_data['status'] = False
        response_data['message'] = "Token invalid | keys missing"
        return Response(data=response_data, status=HTTP_400_BAD_REQUEST)

    try:
        django_user_object = User.objects.get(id=django_id)
    except User.DoesNotExist:
        response_data['status'] = False
        response_data['message'] = "Invalid user ID"
        return Response(data=response_data, status=HTTP_400_BAD_REQUEST)

    if not hasattr(django_user_object, 'lumos_user'):
        response_data['status'] = False
        response_data['message'] = "Lumos User is not registered"
        return Response(data=response_data, status=HTTP_400_BAD_REQUEST)
    else:
        lumos_user_object = django_user_object.lumos_user

    if lumos_user_object.is_verified:
        response_data['status'] = False
        response_data['message'] = "Email is already verified!"
        return Response(data=response_data, status=HTTP_400_BAD_REQUEST)

    # check epoch not beyond 30
    if not epoch_in_future(given_epoch=epoch):
        response_data['status'] = False
        response_data['message'] = "Token expired. Please verify email again"
        return Response(data=response_data, status=HTTP_400_BAD_REQUEST)

    lumos_user_object.is_verified = True
    lumos_user_object.save()

    user_lumos_token = lumos_user_object.lumos_token

    response_data['status'] = True
    response_data['message'] = "User email verified"
    response_data['lumos_token'] = user_lumos_token

    # embed the query params in the url and they can be extracted on the frontend to manipulate the flow
    login_url = HOME_PAGE_URL
    redirect_url = create_query_paramed_url(base_url=login_url, payload=response_data)
    print(redirect_url)

    return Response(data=response_data)
    # return HttpResponsePermanentRedirect(redirected_url)



# to do
# reset password endpoint
# email sendgrid api keys
# env vars in gitignore
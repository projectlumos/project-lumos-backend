from django.conf.urls import url
from rest_framework.routers import DefaultRouter


# project level imports

# app level imports
from accounts.user_account_management.user_account_management_resource import create_lumos_user, logout_lumos_user,\
    verify_user, email_verification_request


router = DefaultRouter()

# router.register(r'^lumos_user', LumosUserViewSet)


urlpatterns = router.urls

urlpatterns += [

    # user auth urls
    url(r'^signup/', create_lumos_user),
    url(r'^logout/', logout_lumos_user),
    url(r'^verify_user/', verify_user),
    url(r'email_verification_request', email_verification_request),
]

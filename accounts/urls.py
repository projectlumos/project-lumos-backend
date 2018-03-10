from django.conf.urls import url
from rest_framework.routers import DefaultRouter


# project level imports

# app level imports
from accounts.user_account_management.user_account_management_resource import create_lumos_user


router = DefaultRouter()

# router.register(r'^lumos_user', LumosUserViewSet)


urlpatterns = router.urls

urlpatterns += [

    # user auth urls
    url(r'^signup/', create_lumos_user),

]

"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from utilities.views import wikiscript, dictscript
from .routers import router

from rest_framework_jwt.views import obtain_jwt_token

from django.conf.urls import include, url
from django.contrib import admin
from feedback.api.views import FeedbackAPIView

# from related.api.views import(
#     KnowledgeBaseRelatedView,
#     SoftSkillsDataRelatedView,
#     RandomDataRelatedView
# )

# TODO REFACTOR NAMESPACES AND URLS

urlpatterns = [
    url(r'^admin/docs/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^auth/login/$', obtain_jwt_token),
    path('wiki/<slug:term>/', wikiscript, name='wiki'),
    path('dict/<slug:term>/', dictscript, name='dictionary'),
    path('api/', include(router.urls)),
    url(r'^api/feedback/', FeedbackAPIView.as_view(), name='feedback'),
    # url(r'^api/knowledgebase-related/(?P<pk>\d+)/$', KnowledgeBaseRelatedView.as_view(), name='kb_related'),
    # url(r'^api/softskills-data-related/(?P<pk>\d+)/$', SoftSkillsDataRelatedView.as_view(), name='ssd_related'),
    # url(r'^api/random-data-related/(?P<pk>\d+)/$', RandomDataRelatedView.as_view(), name='rd_related'),
    url(r'^accounts/', include('accounts.urls')),
]

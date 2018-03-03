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
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from utilities.views import wikiscript, dictscript
# from .routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wiki/<slug:term>/', wikiscript , name='wiki'),
    path('dict/<slug:term>/', dictscript , name='dictionary'),
    # path('api/', include(router.urls)),
    # path('wiki/(?P<term>[-\w]+)/$', utilities.views.wikiscript, name="wiki" )
    # path('dict/(?P<term>[-\w]+)/$', utilities.views.dictscript, name="dict" )
]

"""NGO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from user_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')), # Django builtin login view

    # Views from user_app
    path('', homepage),
    # path('signup/', create_user_view),
    path('signup/', user_create_view, name = 'Signup'),
    path('signup/profile/', user_profile_view),
    path('donationview/', donation_view)

]

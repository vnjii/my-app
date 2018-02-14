"""travel_buddy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, patterns, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.views.generic.base import TemplateView
# from django.core import views as core_views

import travels.views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'home.html'}, name='logout'),
    url(r'^signup/$', travels.views.signup, name='signup'),
    url(r'^list$', travels.views.ListTravelPlan.as_view(), name='travelplan-list'),
    url(r'^new$', travels.views.CreateTravelPlan.as_view(), name='travelplan-new'),
    url(r'^(?P<pk>\d+)/$', travels.views.TravelPlanView.as_view(), name='travelplan-view'),
    # url(r'^admin/', admin.site.urls),
]
from django.conf.urls import url

# from django.contrib import admin
# from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^main/', views.main),
    # url(r'logout/$', views.main),
    url(r'^travels/$', views.travels),
    url(r'^destination/$', views.destination),
    url(r'^add/$', views.add)
]

# urlpatterns = [
#     url(r'^$', views.home, name='home'),
# ]

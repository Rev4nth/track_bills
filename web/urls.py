from django.conf.urls import url

from . import views
from django.contrib.auth import views as auth_views

urlpatterns =  [
    url(r'^$', auth_views.login, kwargs={'template_name':'login.html'} ,name='login'),
    url(r'^logout/$', auth_views.logout, kwargs={'next_page': '/'},name='logout'),
    url(r'^account/$', views.accounts_list, name='accounts_list'),
    url(r'^account/(?P<account_id>[0-9]+)$', views.accounts, name='accounts'),
]

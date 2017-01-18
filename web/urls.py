from django.conf.urls import url
from django.conf.urls.static import  static
from django.conf import settings
from django.contrib.auth import views as auth_views

from . import views


urlpatterns =  [
    url(r'^$', auth_views.login, kwargs={'template_name':'login.html','redirect_authenticated_user': True} ,name='login'),
    url(r'^logout/$', auth_views.logout, kwargs={'next_page': '/'},name='logout'),
    url(r'^account/$', views.accounts_list, name='accounts_list'),
    url(r'^account/(?P<account_id>[0-9]+)$', views.accounts, name='accounts'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

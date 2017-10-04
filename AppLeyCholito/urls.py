from django.conf.urls import include, url
from . import views

urlpatterns = [
      url(r'^index/$', views.index, name='index'),
      url(r'^authentication/$', views.authentication, name='authentication'),
      url(r'^login/$', views.login, name='login'),
      url(r'^denuncia/new/$', views.denuncia_new, name='denuncia_new'),

]
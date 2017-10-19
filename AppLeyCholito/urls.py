from django.conf.urls import include, url
from . import views

urlpatterns = [
      url(r'^$', views.index, name='index'),
      url(r'^register/$', views.authentication, name='authentication'),
      url(r'^login/$', views.login, name='login'),
      url(r'^denuncia/new/$', views.denuncia_new, name='denuncia_new'),
      url(r'^denuncia/(?P<pk>[0-9]+)/$', views.denuncia_detail, name='denuncia_detail')

]
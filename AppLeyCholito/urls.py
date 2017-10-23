from django.conf.urls import include, url
from . import views

urlpatterns = [
      url(r'^$', views.index, name='index'),
      url(r'^register/$', views.UserFormView.as_view(), name='register'),
      url(r'^login/$', views.Login.as_view(), name='login'),
      url(r'^denuncia/new/$', views.denuncia_new, name='denuncia_new'),
      url(r'^denuncia/(?P<pk>[0-9]+)/$', views.denuncia_detail, name='denuncia_detail'),
      url(r'^animal/(?P<pk>[0-9]+)/$', views.animal_detail, name='animal_detail'),
      url(r'^animal/new/$', views.animal_new, name='animal_new')
]
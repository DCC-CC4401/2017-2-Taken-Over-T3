from django.conf.urls import include, url
from . import views

urlpatterns = [
      url(r'^denuncia/new/$', views.denuncia_new, name='denuncia_new'),
]
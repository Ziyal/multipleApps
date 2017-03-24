from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^process$', views.process, name = 'process'),
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name = 'destroy'),
    url(r'^destroy/delete/(?P<id>\d+)$', views.delete, name = 'delete'),
    url(r'^destroy/back$', views.back, name = 'back'),
    url(r'^add_user$', views.add_user, name = 'add_user'),
]

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<username>[a-z]+)/$', views.index, name='index'),
]
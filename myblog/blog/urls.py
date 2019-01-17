from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^hello/$', views.hello, name='hello'),
    url(r'^welcome/(?P<name>\w+)/$', views.welcome, name='welcome'),
    url(r'^$', views.index, name='index'),

]
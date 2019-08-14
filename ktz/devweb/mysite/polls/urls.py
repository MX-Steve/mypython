from django.conf.urls import url
from . import  views


urlpatterns=[
    url(r'^$', views.index,name='index'),
    url(r'^1$',views.details,name='details'),
    url(r'result$',views.result,name='result'),
]
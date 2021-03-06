from django.conf.urls import url, include
from . import views

urlpatterns = [
    # index page,url's name index
    url(r'^$',views.index, name='index'),
    url(r'^(?P<question_id>\d+)/$',views.detail, name='detail'),
    url(r'^(?P<question_id>\d+)/result/$',views.result, name='result'),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<question_id>\d+)/voteact/$',views.voteact, name='voteact')
]
from django.conf.urls import url
from . import views

urlpatterns = [
    url('join/', views.join, name='join'),
    url('', views.index, name='index'),
]
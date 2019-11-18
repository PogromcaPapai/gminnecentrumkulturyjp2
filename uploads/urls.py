from django.conf.urls import url
from django.contrib import admin

from uploads.core import views


urlpatterns = [
    url('^$', views.home, name='home'), 
    url('reserve/', views.reservation, name='reserve'),
    url('register/', views.register, name='registration'),
]

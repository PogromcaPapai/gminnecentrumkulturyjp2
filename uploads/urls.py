from django.conf.urls import url
from django.urls import path
from django.contrib import admin

from uploads.core import views


urlpatterns = [
    url('^$', views.home, name='home'), 
    url('register/', views.register, name='register'),
    url('newshow/', views.showform, name='new_show'),
    url('about/', views.about, name='about'),
    url('contact/',views.contact, name='contact'),
    path('show/<int:show>/<int:column>/<int:row>/', views.reservation, name='reserve'),
    path('show/<int:show>/', views.showdetails, name='details'),
    url('show/', views.showlist, name='event_list')
]

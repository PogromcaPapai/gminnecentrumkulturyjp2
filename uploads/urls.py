from django.conf.urls import url
from django.contrib import admin

from uploads.core import views


urlpatterns = [
    url('^$', views.home, name='home'), 
    url('register/', views.register, name='register'),
    url('show/<int:show>/<int:place>/', views.reservation, name='registration'),
    url('show/<int:show>/', views.showplaces, name='show_data')
]

from django.conf.urls import include, url
from django.contrib import admin

from dashboard import views

urlpatterns = [
    url(r'^home', views.home, name='Home'),  
    url(r'^cierreToPDF/', views.campaignsToPDF),  
    
]

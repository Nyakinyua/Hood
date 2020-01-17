from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    url(r'^logout/$',views.logout,name='logout'),
    
]
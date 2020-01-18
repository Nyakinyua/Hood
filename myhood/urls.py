from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    url(r'^logout/$',views.logout_user,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('edit/',views.update_profile,name="edit"),
]
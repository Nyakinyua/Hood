from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    url(r'^logout/$',views.logout_user,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('edit/',views.update_profile,name="edit"),
    path('post/',views.add_post,name="post"),
    path('search/',views.search_results,name="search"),
    path('biz/',views.new_business,name="new_biz"),
    path('business/',views.view_business,name='business'),
]
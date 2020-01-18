from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group

# Register your models here.
admin.site.site_header = 'Admin Trial Dashboard'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','bio','pic','contact','location')
    

admin.site.register(Neighborhood)
admin.site.register(Business)
admin.site.register(Department)
from django import forms
from .models import *
from pyuploadcare.dj.forms import ImageField
from django.contrib.auth.models import User


class UpdateProfileForm(forms.ModelForm):
    '''
    class that define how the update profile form will look like
    '''
    class Meta:
        model = Profile
        exclude = ['user']
        

        
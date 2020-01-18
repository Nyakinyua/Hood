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
        
class NewPostForm(forms.ModelForm):
    '''
    Class that define how the new post form will look like
    '''
    class Meta:
        model = Posts
        exclude = ['posted_by']
        
class NewBizForm(forms.ModelForm):
    """
    class that defines how the business form looks like
    """
    class Meta:
        model = Business
        exclude = ['owner']
        

        
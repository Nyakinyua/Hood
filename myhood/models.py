from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import Imagefield


# Create your models here.
class Profile(models.Model):
    '''
    Class that creates instance of a new user
    '''


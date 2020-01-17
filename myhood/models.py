from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField


# Create your models here.
class Neighborhood(models.Model):
    '''
    Class that creates neighborhood objects
    '''
    loc_name = models.CharField(max_length = 400)
    location = models.CharField(max_length=700)
    
    def __str__(self):
        return self.loc_name
    
class Profile(models.Model):
    '''
    Class that creates instance of a new user
    '''
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField()
    location = models.CharField(max_length=200)
    bio = models.CharField(max_length=500)
    pic = ImageField(blank=True,manual_crop="")
    
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
class Business(models.Model):
    '''
    class that creates instance of a new business
    '''
    bs_name = models.CharField(max_length=300)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    locality = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    bs_email = models.EmailField()
    
    def __str__(self):
        return self.bs_name
    
    
    
class Posts(models.Model):
    """
    Class that allows users to create new posts on happenings in their neighborhood
    """
    title = models.CharField(max_length=50)
    image = ImageField(blank=True,manual_crop='')
    description = models.TextField()
    where = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    
    



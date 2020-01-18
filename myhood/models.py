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
    
class department(models.Model):
    
    
class Profile(models.Model):
    '''
    Class that creates instance of a new user
    '''
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=1000)
    pic = ImageField(blank=True,manual_crop="")
    contact = models.CharField(max_length=10,blank=True)
    location = models.CharField(max_length=50,default=None,blank=True,null=True)
    
    
    
    
    
    def __str__(self):
        return self.user.username
    
    def save_profile(self):
        return self.save()
    
class Business(models.Model):
    '''
    class that creates instance of a new business
    '''
    bs_name = models.CharField(max_length=300)
    about = models.TextField(max_length=400,blank=True,default=None)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    bs_email = models.EmailField()
    
    def __str__(self):
        return self.bs_name
    
    @classmethod
    def search_business(cls,search_term):
        business = cls.objects.filter(bs_name__icontains=search_term)
    
    @classmethod
    def get_businesses(cls,hood):
        '''
        function that searches for a businesses by hood
        '''
        biz=cls.objects.filter(hood__icontains=hood)
        return biz
    
    
class Posts(models.Model):
    """
    Class that allows users to create new posts on happenings in their neighborhood
    """
    title = models.CharField(max_length=50)
    image = ImageField(blank=True,manual_crop='')
    description = models.TextField()
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    where = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    
    def save_post(self):
        return self.save()
    
    def delete_post(self):
        post = Post.objects.all().delete()
        return post
    
    @classmethod
    def search_post(cls,search_term):
        post = cls.objects.filter(title__icontains=search_term)
    
    @classmethod
    def get_hood_posts(cls,hood):
        posts = cls.objects.filter(where__icontains=hood)
        return posts
    
    @classmethod
    def get_posts(cls):
        all_posts = cls.objects.all()
        return all_posts



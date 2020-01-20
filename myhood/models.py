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
    
    @classmethod
    def create_hood(self):
        self.save()
        
    
    @classmethod
    def findhood(cls,business_id):
        found = cls.objects.get(id=neighborhood_id)
        return found
    
    @classmethod
    def delete_hood(self):
        hoody = Neighborhood.objects.all().delete()
        return hoody
    
class Department(models.Model):
    
    name = models.CharField(max_length=50)
    depart_pic = ImageField(blank=True,manual_crop='')
    description = models.TextField(max_length=200)
    contact = models.CharField(max_length=10)
    hood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    @classmethod
    def get_dept(cls,loc):
        depts = cls.objects.filter(hood__icontains=loc)
        return depts
    
    @classmethod
    def get_all_dept(cls):
        all_depts = cls.objects.all()
        return all_depts
    
    
    
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
    
    def get_residents(cls,location):
        res = cls.objects.filter(location__icontains=location)
        return res
    
    def get_profiles(cls):
        all_prof = cls.objects.all()
        return all_prof
    
    def delete_profiles(cls):
        del_prof = cls.objects.all().delete()
        return del_prof
    
class Business(models.Model):
    '''
    class that creates instance of a new business
    '''
    bs_name = models.CharField(max_length=300)
    b_pic = ImageField(blank=True,manual_crop='')
    about = models.TextField(max_length=400,blank=True,default=None)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    bs_email = models.EmailField()
    
    def __str__(self):
        return self.bs_name
    
    def create_biz(self):
        self.save()
    
    @classmethod
    def search_business(cls,search_term):
        business = cls.objects.filter(bs_name__icontains=search_term)
        return business
    
    @classmethod
    def get_businesses(cls,hood):
        '''
        function that searches for a businesses by hood
        '''
        biz=cls.objects.filter(hood__icontains=hood)
        return biz
    
    @classmethod
    def get_all_biz(cls):
        all_bs = cls.objects.all()
        return all_bs
    
    def get_biz(cls,id):
        new_biz = cls.objects.get(id=business_id)
        return new_biz
    
    def delete_biz(cls):
        biznes = Business.objects.all().delete()
        return biznes
        
    
  
    
    
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



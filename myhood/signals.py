from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    '''
    This is a function that creates a profile of a user after registration
    '''
    if created:
        profile.objects.create(user=instance)
        
@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    '''
    This is a function that saves the profile after it has been created
    '''
    instance.profile.save()
    

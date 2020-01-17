from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth import logout


# Create your views here.
@login_required
def index(request):
    
    message = "This is the message"
    return render(request,'index.html', {'message':message})

                                                                                                                                                                                                                                                                        
@login_required(login_url="/accounts/login/")
def logout_user(request):
    '''
    view function renders home page once logout
    '''
    
    logout(request)
    return redirect('/')

# @login_required(login_url='/accounts/login')
def profile(request):
    current_user = request.user.id
    prof = Profile.objects.filter(user=current_user)
    messages ="This is the user profile page"
    
    return render(request,'profile.html',{'person':prof,'messages':messages})


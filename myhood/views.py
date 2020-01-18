from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth import logout
from .forms import *


# Create your views here.
@login_required
def index(request):

    message = "This is the message"
    return render(request, 'index.html', {'message': message})


@login_required(login_url="/accounts/login/")
def logout_user(request):
    '''
    view function renders home page once logout
    '''

    logout(request)
    return redirect('/')


@login_required(login_url='/accounts/login')
def profile(request):
    prof = Profile.objects.filter(user=request.user)
    post = Posts.objects.filter(posted_by=request.user)
    messages = "This is the user profile page"

    return render(request, 'profile.html', {'person': prof, 'messages': messages, 'post': post})


@login_required
def update_profile(request):
    if request.method == 'POST':
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if profile_form.is_valid():
            profile.user = request.user
            profile_form.save()
            return redirect('profile')
    else:
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'edit_profile.html', {'profile_form': profile_form})

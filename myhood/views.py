from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth import logout
from .forms import *


# Create your views here.
@login_required(login_url="/accounts/login/")
def index(request):
    business = Business.get_all_biz()
    depts = Department.get_all_dept()
    posts = Posts.get_posts()
    context = {
        'business':business,
        'depts':depts,
        'posts':posts,
        
    }
    return render(request,'index.html',context)


@login_required(login_url="/accounts/login/")
def logout_user(request):
    '''
    view function renders home page once logout
    '''

    logout(request)
    return redirect('/')


@login_required(login_url='/accounts/login')
def profile(request):
    profile = Profile.objects.filter(user=request.user)
    post = Posts.objects.filter(posted_by=request.user)
    messages = "This is the user profile page"

    return render(request, 'profile.html', {'profile': profile, 'messages': messages, 'post': post})


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


@login_required
def add_post(request):
    '''
    View function that renders the add post form
    '''
    if request.method == 'POST':
        post_form = NewPostForm(request.POST, request.FILES)

        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.posted_by = request.user
            post_form.save()
            return redirect('profile')

    else:
        post_form = NewPostForm()
    return render(request, 'new_post.html', {'post_form': post_form})


@login_required(login_url='/accounts/login/')  
def search_results(request):
    if 'business' in request.GET and request.GET['business']:
        search_term = request.GET.get('business')
        results = Business.search_business(search_term)
        message = f'{search_term} search'

        return render(request, 'search.html', {'message': message, 'results': results, 'search_term': search_term})
    else:
        message = "You did not search any Project, please input project name"
        return render(request, 'search.html', {'message': message})

@login_required
def new_business(request):
    '''
    View function that renders to new_biz.html
    '''
    if request.method == 'POST':
        form = NewBizForm(request.POST,request.FILES)
        if form.is_valid():
            biz = form.save(commit=False)
            biz.owner = request.user
            biz.save()
            return redirect('home')
    else:
        title='New Business'
        form = NewBizForm()
        return render(request,'new_biz.html',{'form':form,'title':title})
    
@login_required
def view_business(request):
    """
    View function that renders the businesses available in the neighbohood
    """
    user = Profile.objects.get(user=request.user.id)
    busness = Business.objects.all()
    return render(request,'business.html',{'business':busness})

@login_required
def departments(request):
    dept = Departments.get_dept(request.user.profile.location)
    return render(request,'hoods.html',{'dept':dept})

@login_required
def new_hood(request):
    '''
    function that allows users change their hood once they move
    '''
    if request.method == 'POST':
        form = NewHoodForm(request.POST,request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            return redirect('profile')
    else:
        form = NewHoodForm()
        return render(request,'hood.html',{'form':form})
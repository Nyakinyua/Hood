from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    
    message = "This is the message"
    return render(request,'index.html', {'message':message})

def logout(request):
    '''
    View function that renders to login page once a user signs out
    '''
    logout(request)
    return redirect('/')
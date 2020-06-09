from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

# Function to handle the traffic from our home
# also in this place we decide how we want to handle to routes


def home(request):
    context = {
        'posts':Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)
    
def about(request):
    return render(request, 'blog/about.html',{'title':'About'})

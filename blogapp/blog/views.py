from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# Create your views here.

# Function to handle the traffic from our home
# also in this place we decide how we want to handle to routes

posts = [
    {
        'author':'Soumyajit Rout',
        'title':'Blog post 1',
        'content': 'First post content',
        'date_posted':'June 4 2020'
    },
    {
        'author':'Suman Goel',
        'title':'Blog post 2',
        'content': 'Second post content',
        'date_posted':'June 5 2020'
    },
]

# Function based views

# def home(request):
#     context = {
#         'posts':Post.objects.all(),
#     }
#     return render(request, 'blog/home.html', context)
    

# Classed based views

class PostListView(ListView):
    model = Post # The model we are working on 
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html {default one}
    context_object_name = 'posts' # Value p assed to the template
    ordering = ['-date_posted'] # It decides the sorting
    paginate_by = 2


class PostDetailView(DetailView):
    model = Post # The model we are working on 


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post # The model we are working on 
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Post # The model we are working on 
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        
        return False        


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post # The model we are working on 
    success_url = '/' # redirects to home page when page is deleted
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        
        return False        



def about(request):
    return render(request, 'blog/about.html',{'title':'About'})

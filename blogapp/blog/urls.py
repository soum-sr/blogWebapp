from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'), # Format-> route, function(like flask)
    path('about/', views.about, name='blog-about'),
]

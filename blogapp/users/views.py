from django.shortcuts import render
# To redirect
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
# To display flash messages
from django.contrib import messages

# Create your views here.

# Register view
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)    
        if form.is_valid():
            form.save() # thats it!
            username = form.cleaned_data.get('username')
            # Flash message
            messages.success(request, f'Account Created for {username}. You can now Log In!')
            return redirect('login') # takes the name of url
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html',{'form':form})


# Decorator to make sure that this route is only accessible when the user is logged in
@login_required
def profile(request):
    return render(request, 'users/profile.html')
from django.shortcuts import render
# To redirect
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
# To display flash messages
from django.contrib import messages

# Create your views here.

# Register view
def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)    
        if form.is_valid():
            username = form.cleaned_data.get('username')
            # Flash message
            messages.success(request, f'Account Created for {username}!')
            return redirect('blog-home') # takes the name of url


    else:
        form = UserCreationForm()

    return render(request, 'users/register.html',{'form':form})



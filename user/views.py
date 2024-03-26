from django.contrib.auth import authenticate, login 
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import messages
from .forms import CustomSignupForm

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home.html')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')


def user_signup(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')  # Extract username from POST data
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            if User.objects.filter(username=username).exists():
                return render(request,'signup.html')  
                
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, f'Account created for {username}')

            return render(request,'login.html')  # Redirect to login page after successful signup
        else:
            messages.error(request, 'Invalid signup form. Please check your input.')
    else:
        form = CustomSignupForm()
    return render(request, 'signup.html', {'form': form})


def home(request):

    return render(request, 'home.html')

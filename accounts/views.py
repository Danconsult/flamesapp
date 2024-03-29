from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import SignupForm,LogInForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account is created successfully")
            new_user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1']
            )
            login(request, new_user)
            return redirect('app')
        else:
            messages.error(request,"Error")
    else:
        form = SignupForm()
    return render(request, 'accounts/register.html',{'form':form})

def logIn(request):
    if request.method == "POST":
        form = LogInForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username = username, password = password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f"You are logged in as {username}")
                return redirect('home')
            else:
                messages.error(request, "Error")
        else:
            messages.error(request, "Username or password is incorrect")
    form = LogInForm()
    return render(request, 'accounts/login.html',{'form':form})

def logOut(request):
    logout(request)
    messages.success(request,"You have successfully logged out")
    return redirect('app')


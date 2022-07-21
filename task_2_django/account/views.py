import email
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import AccountAuthenticationForm, SignUpForm
from django.core import serializers
from django.contrib.auth.models import User
from .models import Profile

def index(req):
    if req.user is not None:
        return redirect('dashboard')
    return redirect('login')
    
@login_required(login_url='login')    
def dashboard(req):
    context = {
        "name":req.user.username,
        "phone":Profile.objects.get(user=req.user).phone,
        "email":req.user.email,
    }
    
    return render(req,'Dashboard.html',context)
    pass

def loginUser(req):
    if req.method == 'POST':
        form = AccountAuthenticationForm((req.POST))
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(req, user)
            return redirect('dashboard')
        else:
            return render(req, 'login.html',context={"form":form} )
    context = {
        "form":AccountAuthenticationForm()
    }
    return render(req, 'login.html',context=context )
    pass

def registerUser(req):
    if req.method == 'POST':
        form = SignUpForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            phone = form.cleaned_data.get('phone')
            user = authenticate(username=username, password=raw_password)
            Profile(user=user,phone=phone).save()
            login(req, user)
            return redirect('dashboard')
        else:
            return render(req, 'register.html',context={"form":form} )
    context = {"form":SignUpForm()}
    return render(req, 'register.html',context=context )

def logoutUser(req):
    logout(req)
    return redirect('login')
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

from .forms import LoginForm  # Import login function

# Create your views here.
def index(request):
    return render(request, "ex/index.html", {})

def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = form['username'].value
        password = form['password'].value
        user = authenticate(
            request, 
            username=username, 
            password=password
        )
        if user is not None:
            # Log user in
            login(request, user)
            return redirect('/')
    return render(request, "ex/login.html", { 'form': form })
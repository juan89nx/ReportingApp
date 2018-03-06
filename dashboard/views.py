from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, response

#imports para Roles y Permisos
from django.contrib.auth.decorators import login_required
from rolepermissions.decorators import has_role_decorator
from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect("/login/")

def login(request):
    #return render(request, 'pages/login.html', {})
    return HttpResponseRedirect("/login/")

from django.shortcuts import redirect

@login_required
def login_success(request):
    # Redirects users based on whether they are in the admins group
    if request.user.groups.filter(name="user").exists():
        print (request.user.username)
        # user is an admin
        return redirect("/dashboard/home")
    else:
        context = {
            #'all_ventas': all_ventas,
        } 
        #return render(request, 'pages/home.html', context)
        return redirect("/login/", context)

# Create your views here.

def home(request):
     
     context = {
    
    }
     
     return render(request, 'pages/home.html', context)

#User signup - Registro
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/login/')
    else:
        form = UserCreationForm()
    return render(request, 'pages/signup.html', {'form': form})


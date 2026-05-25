from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
 
def loginUser(request):
    context ={}
    return render(request,'accounts/login.html', context)

def registerUser(request):
    context ={}
    return render(request,'accounts/register.html', context)

def passwordReset(request):
    context ={}
    return render(request,'accounts/password_reset.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login') # this basically instructs django to take you back to login page
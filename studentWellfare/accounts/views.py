from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserForm
from django.contrib import messages # aids in notification/ pop ups 

# Create your views here.
 
def loginUser(request):
    context ={}

    if request.method == 'POST':        
        #  extracting th user inpurt 
        username = request.POST.get("username")
        password = request.POST.get("password")  

        # validate the user exists
        user = authenticate(request,username = username, password = password) 
      
        if user is not None:  
            login(request, user) # login user => creates the user aith session
            messages.info(request, f"Welcome home {username}")
            return redirect('home')
        else:   
            messages.error(request, "check your credentials")
            return redirect('login')
    else:
        pass

    return render(request,'accounts/login.html', context)

def registerUser(request):
    
    if request.method == "POST": 
        form = UserForm(request.POST, request.FILES) # captures both for, input and files

        if form.is_valid(): # check whether form inputs are well done
            user = form.save(commit = False) # pause submission
            user.save() # create the new user
            messages.info(request, "Success!")
            return redirect('login')
        else:
            # form = UserForm() # create an instance of the userform
            messages.info(request, f"Failed! {form.errors}")
    else:
        messages.error(request, "Oops something went wrong")
        form = UserForm()
    context ={"form":form}
    return render(request,'accounts/register.html', context)

def passwordReset(request):
    context ={}
    return render(request,'accounts/password_reset.html', context)

def logoutUser(request):
    logout(request)
    messages.info(request, "Successfully logged you out!")
    return redirect('login') # this basically instructs django to take you back to login page
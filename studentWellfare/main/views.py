from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReportForm, AppointmentForm, FeedbackForm, ResourceForm, NotificationForm
from django.contrib import messages # aids in notification/ pop ups 

# Create your views here.
@login_required(login_url='login')
def home(request):
    context ={} 
    print(request.user)
    return render(request, 'home.html', context)
    
@login_required(login_url='login')
def userProfile(request):
    context = {}  
    return render(request, 'main/userprofile.html', context)

@login_required(login_url='login')
def createReport(request):
    form = ReportForm() # instance of the form 
    context = {"form": form, "type": "Report"}
    return render(request, 'main/forms.html', context)


@login_required(login_url='login')
def bookAppointment(request):
    form = AppointmentForm() # instance of the form 
    context = {"form": form, "type": "Book an AppointmentForm"}
    return render(request, 'main/forms.html', context)


@login_required(login_url='login')
def createFeedback(request):
    form = ResourceForm() # instance of the form 
    context = {"form": form, "type": "How was your appointment? "}
    return render(request, 'main/forms.html', context)


@login_required(login_url='login')
def createResource(request):
    if request.method == "POST": 
        form = ResourceForm(request.POST, request.FILES) # captures both for, input and files

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
        form = ResourceForm() 
    context = {"form": form, "type": "Add a new resource"}
    return render(request, 'main/forms.html', context)



@login_required(login_url='login')
def createNotification(request):
    form = NotificationForm() # instance of the form 
    context = {"form": form, "type": "Notify users of something new!"}
    return render(request, 'main/forms.html', context)

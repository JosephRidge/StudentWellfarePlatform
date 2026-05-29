from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('user-profile/',views.userProfile, name='user-profile'),

# Reports CRUD
    path('create-report/',views.createReport, name='create-report'),


# APPOINTMENTS CRUD
    path('book-appointment/',views.bookAppointment, name='book-appointment'),


# FEEBACK CRUD
    path('create-feedback/',views.createFeedback, name='create-feedback'),


# RESEOUCE CRUD    
    path('create-resource/',views.createResource, name='create-resource'),


# NOTIFICAITON CRUD 
    path('create-notification/',views.createNotification, name='create-notification'),

]
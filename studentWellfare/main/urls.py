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


# RESEOURCE CRUD    
    path('create-resource/',views.createResource, name='create-resource'),
    path('read-resource/<int:pk>',views.readResource, name='read-resource'),
    path('read-resources/',views.readResources, name='read-resources'),
    path('update-resource/<int:pk>',views.updateResources, name='update-resources'),
    path('delete-resource/',views.deleteResources, name='delete-resources'),


# NOTIFICAITON CRUD 
    path('create-notification/',views.createNotification, name='create-notification'),

]
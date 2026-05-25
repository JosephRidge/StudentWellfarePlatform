from django.urls import path 
from . import views # import the view function


urlpatterns = [
    path('login/', views.loginUser, name ="login"),
    path('register/', views.registerUser, name ="register"),
    path('logout/', views.logoutUser, name ="logout"),
    path('forgot-password/', views.passwordReset, name ="forgot-password/"),
]
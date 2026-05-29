from django.db import models
from django.contrib.auth.models import AbstractUser # helps in customization of User themselves

# Create your models here.

class User(AbstractUser):

    ROLE_CHOICES ={
        "student": "Student", 
        "officer":"Welfare Officer", 
        "counsellor": "Counsellor",
        "lecturer":"Lecturer"
    }

    roles = models.CharField(max_length=100, choices=ROLE_CHOICES, default="student")
    bio = models.TextField(blank = True)
    profile_picture = models.ImageField(upload_to="profile_pictures", blank=True) 
    create_at = models.DateTimeField(auto_now = True) 
    updated_at = models.DateTimeField(auto_now_add = True)
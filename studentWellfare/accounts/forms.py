from django.contrib.auth.forms import UserCreationForm  
from .models import User 

class UserForm(UserCreationForm):
    class Meta: 
        model = User 
        fields = UserCreationForm.Meta.Fields + ("first_name", "last_name","email", "roles", "bio","profile_picture")
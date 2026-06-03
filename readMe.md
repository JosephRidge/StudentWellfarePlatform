## set-up 

- to attain the needed libraries run `pip install -r requirements.txt`
- configure templates, static and media (all this will be done in `setting.py`):
    - Templates (add ` 'DIRS': [BASE_DIR / 'templates'],` inside the TEMPLATES config): 
    ```
            TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [BASE_DIR / 'templates'],
                'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                    ],
                },
            },
        ]
    ```

    - static & media  config: 
        ```
        STATIC_URL = 'static/'
        STATICFILES_DIRS = [
            BASE_DIR / "static",
            "/var/www/static/",
        ]

        MEDIA_URL = '/media/'
        MEDIA_ROOT = BASE_DIR / 'media'
        ```
    
    - update `urls.py` (project level):

        ```
            from django.contrib import admin
            from django.urls import path
            from django.conf import settings 
            from django.conf.urls.static import static


            urlpatterns = [
                path('admin/', admin.site.urls),
            ]
            if settings.DEBUG:
                urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        ``` 

TODO: Add each step of implementation


## Auth Set-up

- add this in your `setting.py`:  `AUTH_USER_MODEL = 'accounts.User'`

- Create `user-model`:
    - We bring in the abstractuser since we want to customize the user details
    ``` {py}

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

    ```

- create the userForm: 
    - create the `forms.py` file
    - create the `UserForm`: 
        ```
        from django.contrib.auth.forms import UserCreationForm  # embracing the prebuilt UserCreationForm
        from .models import User # importing the Model

        class UserForm(UserCreationForm):
            class Meta: 
                model = User 
                fields = UserCreationForm.Meta.Fields + ("first_name", "last_name","email", "roles","profile_picture","bio")

        ```


# Database Structure:
![alt text](image.png)
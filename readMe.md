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
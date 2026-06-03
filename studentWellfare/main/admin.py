from django.contrib import admin
from .models import Report,Appointment,Feedback,Resource,Notification

# Register your models here.
admin.site.register(Report) 
admin.site.register(Appointment)
admin.site.register(Feedback)
admin.site.register(Resource)
admin.site.register(Notification)
from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class Report(models.Model): 

    CATEGORY_CHOICES = [
        ("academic","ACADEMIC"), 
        ("mental_health", "MENTAL HEALTH"),
        ("physical_health", "PHYSICAL HEALTH"),
        ("security", "SECURITY"),
        ("financial", "FINANCIAL"),
        ("other", "OTHER")
    ]

    URGENCY_CHOICES = [
        ("low","LOW"), 
        ("medium", "MEDIUM"),
        ("high", "HIGH")
    ]
    
    STATUS_CHOICES = [
            ("pending","PENDING"), 
            ("in_review", "IN REVIEW"),
            ("resolved", "RESOLVED"),
            ("closed", "CLOSED")
        ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True) # 1-many relationship
    title = models.CharField(max_length=100)
    description = models.TextField() 
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default="security") 
    urgency = models.CharField(max_length=100, choices=URGENCY_CHOICES, default="medium") 
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="pending") 
    evidence_one = models.ImageField(upload_to="report_evidence", blank=True) 
    create_at = models.DateTimeField(auto_now = True) 
    updated_at = models.DateTimeField(auto_now_add = True)



class Appointment(models.Model):  
    SPEICALIST_CHOICES = [
            ("counsellor","COUNSELOR"), 
            ("lecturer", "LECTURER"),
            ("peer_mentor", "PEER MENTOR"),
            ("other", "OTHER")
        ]

    STATUS_CHOICES = [
                ("scheduled","SCHEDULED"), 
                ("completed", "COMPLETED"),
                ("cancelled", "CANCELLED"),
                ("did_not_show", "DID NOT SHOW UP")
            ]

    report = models.ForeignKey(Report, on_delete=models.SET_NULL, null=True) 
    notes = models.TextField()
    date_time = models.DateTimeField() 
    duration_minutes = models.IntegerField(default=15)
    specialist_to_see = models.CharField(max_length=100, choices=SPEICALIST_CHOICES, default="counselor")
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="scheduled") 
    create_at = models.DateTimeField(auto_now = True) 
    updated_at = models.DateTimeField(auto_now_add = True)

class Feedback(models.Model):
    report  = models.ForeignKey(Appointment, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comments = models.TextField()
    create_at = models.DateTimeField(auto_now = True) 
    updated_at = models.DateTimeField(auto_now_add = True)

 
class Resource(models.Model):
    CATEGORY_CHOICES = [
            ("academic","ACADEMIC"), 
            ("mental_health", "MENTAL HEALTH"),
            ("physical_health", "PHYSICAL HEALTH"),
            ("security", "SECURITY"),
            ("financial", "FINANCIAL"),
            ("other", "OTHER")
        ]
    
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default="security") 
    title= models.CharField(max_length=150)
    notes = models.TextField()
    link = models.CharField(max_length=150)
    image = models.ImageField(upload_to="resource_images", blank=True, null=True)
    image_two= models.ImageField(upload_to="resource_images", blank=True, null=True)
    file = models.FileField(upload_to="resource_file", blank=True, null=True)
    create_at = models.DateTimeField(auto_now = True) 
    updated_at = models.DateTimeField(auto_now_add = True)

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now = True) 
    updated_at = models.DateTimeField(auto_now_add = True)
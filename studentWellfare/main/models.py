from django.db import models
from django.conf import settings

class Report(model.Models): 

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

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL) # 1-many relationship
    title = models.CharField(max_length=100)
    description = models.TextField() 
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default="security") 
    urgency = models.CharField(max_length=100, choices=URGENCY_CHOICES, default="medium") 
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="pending") 
    evidence_one = models.ImageField(upload_to="report_evidence", blank=True) 
    create_at = models.DateTimeField(auto_now = True) 
    updated_at = models.DateTimeField(auto_now_add = True)
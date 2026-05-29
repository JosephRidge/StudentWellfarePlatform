
from .models import Report,Appointment,Feedback,Resource,Notification
from django.forms import ModelForm


class ReportForm(ModelForm):
    class Meta: 
        model = Report
        fields = '__all__'


class AppointmentForm(ModelForm):
    class Meta: 
        model = Appointment
        fields = '__all__'


class FeedbackForm(ModelForm):
    class Meta: 
        model = Feedback
        fields = '__all__'


class ResourceForm(ModelForm):
    class Meta: 
        model = Resource
        fields = '__all__'

class NotificationForm(ModelForm):
    class Meta: 
        model = Notification
        fields = '__all__'


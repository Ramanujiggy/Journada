from django import forms 
from .models import Session 



class TrainingSessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['date', 'hours_trained', 'minutes_trained', 'notes', 'time', 'grappling_type', ]
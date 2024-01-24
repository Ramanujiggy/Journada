from django import forms 
from .models import GrappleEntry



class TrainingSessionForm(forms.ModelForm):
    class Meta:
        model = GrappleEntry
        fields = ['date', 'hours_trained', 'minutes_trained', 'notes', 'time', 'grappling_type', ]
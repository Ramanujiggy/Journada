from django import forms 



class LogUserSessionForm(forms.Form):
    date=forms.DateTimeField(input_formats=['%d/%m/%y %H:%M'])

from django import forms 

class RegisterUserForm(forms.Form):
    user_email=forms.CharField(label='Email Address:', max_length=100)
    username=forms.CharField(label='Username:',max_length=30)
    password=forms.CharField(label='Password',max_length=50)



class LogUserSessionForm(forms.Form):
    date=forms.DateTimeField(input_formats=['%d/%m/%y %H:%M'])

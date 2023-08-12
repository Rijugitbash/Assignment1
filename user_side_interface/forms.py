from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)



class ApplicationForm(forms.Form):
    choices = [
        ('application type 1', 'application type 1'),
        ('application type 2', 'application type 2'),
        ('application type 3', 'application type 3'),
    ]

    select_application_type = forms.ChoiceField(choices=choices, widget=forms.Select(attrs={'class': 'form-select'}))
    service_details = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    attach_file = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))

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
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
    ]

    select_field = forms.ChoiceField(choices=choices, widget=forms.Select(attrs={'class': 'form-select'}))
    text_field = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    file_field = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))

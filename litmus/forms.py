from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Profile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100,help_text='Last Name')
    last_name = forms.CharField(max_length=100,help_text='Last Name')
    email = forms.EmailField(max_length=150,help_text='Email')

    class Meta:
        model = User
        fields = ('username','first_name','last_name',
        'email','password1','password2',)
        
#class LogInForm(forms.ModelForm):
    #email = forms.EmailField(max_length=150,help_text='Email')
    #class Meta:
    #    model = User
    #    fields = ('email','password1',)

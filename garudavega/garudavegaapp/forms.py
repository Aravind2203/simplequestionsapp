from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class RegisterUser(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class Additem(forms.Form):
    answer=forms.Textarea()
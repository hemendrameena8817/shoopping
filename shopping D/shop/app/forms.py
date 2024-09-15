from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm , UsernameField
from django.contrib.auth.models import User 
from django.utils.translation import gettext, gettext_lazy as _
class CustomeRegistrationFrom(UserCreationForm):
 password1 =  forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
 password2 = forms.CharField(label='Confirm password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
 email = forms.EmailField(required=True, widget=forms.EmailInput
(attrs={'class':'form-control'}))
 
 class Meta:
  model = User
  fields =  ['username', 'email','password1', 'password2']
  lables =  {'email': 'Email'}
  widgets = {'username': forms.TextInput(attrs={'class': 'form-control'})}

class LoginForm(AuthenticationForm):
 username = UsernameField(widget = forms.TextInput(attrs=
  {'autofocus':True, 'class': 'form-control'}))
 password = forms.CharField(label=_("Password"), strip=False,
 widget=forms.PasswordInput(attrs=
{'autocomplete': 'current-password', 'class':'form-control'}))
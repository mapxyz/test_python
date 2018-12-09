from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from .models import News

class LoginForm(forms.Form):
    login = forms.CharField(label='Login', max_length=30)
    password = forms.CharField(label='password', max_length=30)

class CreateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'text',)
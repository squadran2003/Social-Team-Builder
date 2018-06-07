from django.forms import inlineformset_factory
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User
import datetime
import re
import os


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['display_name', 'email']
    
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''


class PeofileCreateForm(ModelForm):
    
    class Meta:
        model = User
        fields = ['full_name', 'bio', 'image']


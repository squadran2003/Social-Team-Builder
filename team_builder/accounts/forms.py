from django.forms import inlineformset_factory
from django.forms import ModelForm
from .models import User
import datetime
import re
import os


class UserCreateForm(ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'bio', 'image']






		




	




from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, ProfileImage
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.conf import settings
import datetime, re, os
from PIL import Image


class UserCreateForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['full_name','bio']

class ProfileImageForm(ModelForm):
	class Meta:
		model = ProfileImage
		fields = ['image']



		




	



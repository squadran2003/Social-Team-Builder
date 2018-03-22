from django.contrib import admin
from django.conf import settings

# Register your models here.
from .models import User, ProfileImage



admin.site.register(User)
admin.site.register(ProfileImage)


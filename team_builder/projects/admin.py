from django.contrib import admin

# Register your models here.
from .models import Project, Position
admin.site.register(Project)
admin.site.register(Position)


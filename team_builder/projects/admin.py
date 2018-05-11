from django.contrib import admin

# Register your models here.
from .models import Project, Position, UserCompletedProject
admin.site.register(Project)
admin.site.register(Position)
admin.site.register(UserCompletedProject)


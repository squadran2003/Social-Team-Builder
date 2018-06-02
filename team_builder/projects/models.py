from django.db import models
from django.utils import timezone
from accounts.models import User
from skills.models import Skill


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='projects')
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(default='')
    timeline = models.TextField(default='')
    requirements = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    

class Position(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(default='')
    projects = models.ManyToManyField(Project)
    skills = models.ManyToManyField(Skill,default=None)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
        ordering = ['-created_at']


class UserCompletedProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    url = models.URLField(null=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title



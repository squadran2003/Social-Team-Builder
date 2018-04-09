from django.db import models
from django.utils import timezone
from accounts.models import User

# Create your models here.

class Project(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,
                            related_name='projects')
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(default='')
    timeline = models.TextField(default='')
    requirements = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']


class Position(models.Model):
    project = models.ManyToManyField(Project)
    title = models.CharField(max_length=100)
    description = models.TextField(default='')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


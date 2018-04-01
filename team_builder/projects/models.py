from django.db import models
from django.utils import timezone
from accounts.models import User

# Create your models here.

class Project(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,
                            related_name='projects')
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


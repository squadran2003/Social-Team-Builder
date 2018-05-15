from django.db import models
from django.utils import timezone
from accounts.models import User

# Create your models here.

class Skill(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

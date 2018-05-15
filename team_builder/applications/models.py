from django.db import models
from django.utils import timezone
from accounts.models import User
from projects.models import Position, Project

# Create your models here.
class Application(models.Model):
    user = models.ManyToManyField(User)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    applied_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-applied_on']
    
    def __str__(self):
        return "Application no {}".format(str(self.pk))
    


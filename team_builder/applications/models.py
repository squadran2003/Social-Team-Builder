from django.db import models
from django.utils import timezone
from accounts.models import User
from projects.models import Position, Project

# Create your models here.
class Application(models.Model):
    employer = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='employer')
    position = models.ForeignKey(Position,
                                on_delete=models.CASCADE,
                                related_name='position')
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE,
                                related_name='project')
    employee = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='employee')
    accepted = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    applied_on = models.DateTimeField(default=timezone.now)


    class Meta:
        ordering = ['-applied_on']
    
    def __str__(self):
        return "Application no {}".format(str(self.pk))
    


from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse_lazy
from projects.models import Project

class ProjectHomeView(ListView):
    model = Project
    context_object_name = 'projects'
    fields = ('title','requirements')
    template_name = 'index.html'



    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Project.objects.filter(user=self.request.user)
        else:
            return Project.objects.all()
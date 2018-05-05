from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse_lazy
from projects.models import Project, Position

class ProjectHomeView(ListView):
    model = Project
    context_object_name = 'projects'
    fields = ('title','requirements')
    template_name = 'index.html'



    def get_queryset(self):
        return Project.objects.all().prefetch_related('position_set')
    
    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        data['positions']= Position.objects.all()
        data['filter']= 'All Needs'
        return data
    

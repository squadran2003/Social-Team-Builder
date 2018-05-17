from django.shortcuts import render
from django import forms
from django.contrib import messages
from django.views.generic import CreateView

from django.urls import reverse_lazy
from django.shortcuts import render_to_response

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Application
from projects.models import Position, Project
# Create your views here.

class CreateApplicationView(LoginRequiredMixin, CreateView):
    model = Application
    fields = ()
    template_name = 'projects/project_detail.html'

    def get_success_url(self):
        return reverse_lazy('projects:detail',
                            kwargs={'pk':self.kwargs.get('project_id')}
                            )
    
    
    def form_valid(self, form):
        """check if the logged in user has
         has already applied for a given position
        """
        position = Position.objects.get(pk=self.kwargs.get('position_id'))
        if position.application_set.filter(user=self.request.user).exists():
            messages.error(self.request,'You have already applied for this position')
            raise forms.ValidationError(_("error"),code='invalid')
        else:
            instance = form.save(commit=False)
            instance.position = position
            instance.save()
            instance.user.add(self.request.user)
            instance.save()
        return super().form_valid(form)
    






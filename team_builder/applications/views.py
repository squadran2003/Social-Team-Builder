from django.forms.utils import ErrorList
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import CreateView, ListView, UpdateView

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from notifications.signals import notify

from .models import Application
from projects.models import Project, Position
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
        instance = form.save(commit=False)
        position = Position.objects.get(pk=self.kwargs.get('position_id'))
        project = Project.objects.get(pk=self.kwargs.get('project_id'))
        employer = project.user
        """check to see if a user has already applied for a position"""
        if Application.objects.filter(position=position,
                                      employee=self.request.user).exists():
            messages.error(self.request, 
                           "You have already applied for that position!"
                           )
            return HttpResponseRedirect(reverse_lazy('projects:detail',
                                        kwargs={'pk': 
                                                self.kwargs.get('project_id')
                                                }
                            ))
        else:
            # check if a application
            instance.project = project
            instance.position = position
            instance.employee = self.request.user
            instance.employer = employer
            instance.save()
            message = "Application for job {}".format(
                                                  instance.position
                                                )
            notify.send(instance.employee, 
                        recipient=instance.employer, 
                        verb=message)
            messages.success(self.request, 
                             "Congrats you applied for that position!"
                             )
            return super().form_valid(form)
        

class ListApplicationView(LoginRequiredMixin, ListView):
    model = Application
    fields = ()
    template_name = 'applications/applications.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Application.objects.filter(employer=self.request.user)
        print(queryset)
        return queryset
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['projects'] = Project.objects.filter(user=self.request.user)
        return data


class EditApplicationView(LoginRequiredMixin, UpdateView):
    model = Application
    fields = ['accepted', 'rejected']
    success_url = reverse_lazy('applications:list') 
    template_name = 'applications/application_edit.html'   

    def get_success_url(self):
        messages.success(self.request, "application has been updated!")
        return reverse_lazy('applications:list')
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        print(instance.accepted)
        print(instance.rejected)
        return super().form_valid(form)








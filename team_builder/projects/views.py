from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from .models import Project
from .forms import ProjectPositionFormset

# Create your views here.

class CreateProjectView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ('title','description','timeline','requirements')
    success_url = reverse_lazy('home')

    
    def get_form(self, *args, **kwargs):
        form = super(CreateProjectView, self).get_form(*args, **kwargs)
        form.fields['title'].widget.attrs['placeholder']='Title'
        form.fields['title'].label=''
        form.fields['description'].widget.attrs['placeholder']='description'
        form.fields['description'].label=''
        return form 
    
    def get_context_data(self, **kwargs):
        data = super(CreateProjectView,self).get_context_data(**kwargs)
        if self.request.POST:
            data['positions']= ProjectPositionFormset(self.request.POST)
        else:
            data['positions']=ProjectPositionFormset(instance=self.get_object())
        return data
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateProjectView,self).form_valid(form)
    



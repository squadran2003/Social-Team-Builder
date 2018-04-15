from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from .models import Project
from .forms import PositionFormset

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
            data['formset']= PositionFormset(self.request.POST)
        else:
            data['formset']=PositionFormset()
        return data
    
    def form_valid(self, form):
        data = self.get_context_data()
        positions = data['formset'].save(commit=False)
        if positions.is_valid():
            for position in positions:
                position.project = form.instance
                position.save()
        form.instance.user = self.request.user
        return super(CreateProjectView,self).form_valid(form)
    



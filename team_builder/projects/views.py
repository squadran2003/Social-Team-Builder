from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from .models import Project, Position
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
            data['positions_formset']= PositionFormset(self.request.POST)
        else:
            data['positions_formset']=PositionFormset(queryset=Position.objects.none())
            data['positions_formset'].extra=1
        return data
    
    def form_valid(self, form):
        data = self.get_context_data()
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        positions_formset = data['positions_formset']
        if positions_formset.is_valid():
            positions = positions_formset.save(commit=False)
            for position in positions:
                # check if position exists
                try:
                    '''if it exists just had the projects dont
                    create a new position
                    '''
                    exis_position = Position.objects.get(title=position.title)
                except Position.DoesNotExist:
                    #position doesnt exist, add it and its projects
                    position.save()
                    position.projects.add(instance)
                    position.save()
                else:
                    # only add the projects not the position
                    exis_position.projects.add(instance)
                    exis_position.save()
        return super(CreateProjectView,self).form_valid(form)

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    fields = ('title','description')
    context_object = 'project'

class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'projects/project_edit.html'
    fields = ('title','description','timeline','requirements')
    success_url = reverse_lazy('home')



    def get_form(self, *args, **kwargs):
        form = super(ProjectUpdateView, self).get_form(*args, **kwargs)
        form.fields['title'].widget.attrs['class']='circle--input--h1'
        return form 
    
    # def get_success_url(self):
    #     instance = self.get_object()
    #     return reverse_lazy('projects:detail',kwargs={'pk':instance.pk})
    
    def get_context_data(self, **kwargs):
        data = super(ProjectUpdateView,self).get_context_data(**kwargs)
        project = Project.objects.get(pk=self.kwargs.get('pk'))
        if self.request.POST:
            data['positions_formset']= PositionFormset(self.request.POST)

        else:
            data['positions_formset']=PositionFormset(queryset=Position.objects.filter(
                projects=project
            ))
        return data
    
    def form_valid(self, form):
        data = self.get_context_data()
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        positions_formset = data['positions_formset']
        if positions_formset.is_valid():
            print("check if formset is valid")
            positions = positions_formset.save(commit=False)
            for position in positions:
                position.save()
        return super(ProjectUpdateView,self).form_valid(form)


class PositionFilterView(ListView):
    model = Project
    fields = ('title','description')
    context_object = 'projects'
    success_url = 'home'
    template_name = 'index.html'

    def get_queryset(self):
        filter_val = self.kwargs.get('filter')
        if filter_val=='All Needs':
            return Project.objects.all()
        return Project.objects.filter(position__title=filter_val)

    
    def get_context_data(self, **kwargs):
        data = super(PositionFilterView,self).get_context_data(**kwargs)
        data['projects'] = self.get_queryset()
        data['positions']= Position.objects.all()
        data['filter']= self.kwargs.get('filter')
        return data

class UpdatePositionAppliedStatus(UpdateView):
    model = Position
    fields = ('applied',)
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        position = form.save(commit=False)
        position.applied = True
        position.save()
        position.applicant.add(self.request.user)
        position.save()

        return super().form_valid(form)
    


    



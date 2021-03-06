from django.views.generic import (CreateView, ListView, 
                                  DetailView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q



from .models import Project, Position
from .forms import PositionFormset


class CreateProjectView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ('title', 'description', 'timeline', 'requirements')
    success_url = reverse_lazy('home')

    def get_form(self, *args, **kwargs):
        form = super(CreateProjectView, self).get_form(*args, **kwargs)
        form.fields['title'].widget.attrs['placeholder'] = 'Title'
        form.fields['title'].label = ''
        form.fields['description'].widget.attrs['placeholder'] = 'description'
        form.fields['description'].label = ''
        return form
    
    def get_context_data(self, **kwargs):
        data = super(CreateProjectView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['positions_formset'] = PositionFormset(
                                                    self.request.POST
                                                    )
        else:
            data['positions'] = Position.objects.all()
            data['positions_formset'] = PositionFormset(
                                            queryset=Position.objects.none()
                                        )
            data['positions_formset'].extra = 1
        return data
    
    def form_valid(self, form):
        data = self.get_context_data()
        instance = form.save(commit=False)
        instance.user = self.request.user
        positions_formset = data['positions_formset']
        instance.save()
        if positions_formset.is_valid():
            positions = positions_formset.save(commit=False)
            for obj in positions_formset.deleted_objects:
                obj.projects.remove(instance)
            for position in positions:
                try:
                    exis_pos = Position.objects.get(
                                title=position.title
                    )
                except Position.DoesNotExist:
                    position.save()
                    position.projects.add(instance)
                    position.save()
                else:
                    exis_pos.projects.add(instance)
                    exis_pos.save()
            positions_formset.save_m2m()
        else:
            return HttpResponseRedirect(reverse_lazy('projects:add'))
        return super().form_valid(form)


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    fields = ('title', 'description')
    context_object = 'project'

        
class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'projects/project_edit.html'
    fields = ('title', 'description', 'timeline', 'requirements')
    success_url = reverse_lazy('home')

    def get_form(self, *args, **kwargs):
        form = super(ProjectUpdateView, self).get_form(*args, **kwargs)
        form.fields['title'].widget.attrs['class'] = 'circle--input--h1'
        return form 
    
    def get_success_url(self):
        instance = self.get_object()
        return reverse_lazy('projects:detail', kwargs={'pk': instance.pk})
    
    def get_context_data(self, **kwargs):
        data = super(ProjectUpdateView, self).get_context_data(**kwargs)
        project = Project.objects.get(pk=self.kwargs.get('pk'))
        queryset = Position.objects.filter(projects=project)
        data['positions'] = Position.objects.all()
        if self.request.POST:
            data['positions_formset'] = PositionFormset(self.request.POST)
        else:
            if queryset:
                data['positions_formset'] = PositionFormset(queryset=queryset)
            else:
                # if there are no position send a extra form
                data['positions_formset'] = PositionFormset(queryset=queryset)
                data['positions_formset'].extra = 1
        return data
    
    def form_valid(self, form):
        data = self.get_context_data()
        instance = form.save(commit=False)
        instance.user = self.request.user
        positions_formset = data['positions_formset']
        instance.save()
        # get all positionss
        if positions_formset.is_valid():
            positions = positions_formset.save(commit=False)
            for obj in positions_formset.deleted_objects:
                obj.projects.remove(instance)
            for position in positions:
                try:
                    exis_pos = Position.objects.get(
                                title=position.title
                    )
                    exis_pos.title = position.title
                    exis_pos.description = position.description
                    exis_pos.skill = position.skill
                except Position.DoesNotExist:
                    position.save()
                    position.projects.add(instance)
                    position.save()
                else:
                    exis_pos.projects.add(instance)
                    exis_pos.save()
            positions_formset.save_m2m()
        return super().form_valid(form)


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = 'home'
    template_name = 'projects/project_delete.html'
    context_object = 'project'

    def get_success_url(self):
        messages.success(self.request, "Project has been delete!")
        return reverse_lazy('home')


class PositionFilterView(ListView):
    model = Project
    fields = ('title', 'description')
    context_object = 'projects'
    success_url = 'home'
    template_name = 'index.html'

    def get_queryset(self):
        filter_val = self.kwargs.get('filter')
        if filter_val == 'All Needs':
            return Project.objects.all()
        return Project.objects.filter(position__title=filter_val)

    def get_context_data(self, **kwargs):
        data = super(PositionFilterView, self).get_context_data(**kwargs)
        data['projects'] = self.get_queryset()
        data['positions'] = Position.objects.all()
        data['filter'] = self.kwargs.get('filter')
        return data


class PositionSearchView(ListView):
    model = Project
    fields = ('title', 'description')
    context_object = 'projects'
    success_url = 'home'
    template_name = 'index.html'

    def get_queryset(self):
        search_val = self.request.GET.get('search')
        return Project.objects.filter(
                        Q(title__icontains=search_val) |
                        Q(position__title__icontains=search_val)
                ).distinct()

    def get_context_data(self, **kwargs):
        data = super(PositionSearchView, self).get_context_data(**kwargs)
        data['projects'] = self.get_queryset()
        search_val = self.request.GET.get('search')
        data['positions'] = Position.objects.filter(
                            Q(projects__title__icontains=search_val) |
                            Q(title__icontains=search_val)
                        ).distinct()
        data['search_val'] = search_val
        return data


    


    



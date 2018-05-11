from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from PIL import Image
from django.conf import settings
from . import forms
from projects.forms import UserCompletedProjectFormset
from skills.forms import SkillFormset
from .models import User
from skills.models import Skill
from projects.models import UserCompletedProject



class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    success_url = reverse_lazy('home')
    form_class = forms.UserCreateForm
    context_object = 'user'
 

    def get_object(self):
        return User.objects.get(pk=self.request.user.id)
 
    def get_template_names(self):
        """this method checks the option,
        if its not view it shows the edit template"""
        option = self.kwargs.get('option')
        if not option == None:
            return 'accounts/profile.html'
        else:
             return 'accounts/edit_profile.html'
    
    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['UserCompletedProjects']= UserCompletedProjectFormset(
                                            self.request.POST)
            data['SkillsFormset'] = SkillFormset(
                                            self.request.POST)
        else:
            data['UserCompletedProjects']= UserCompletedProjectFormset()
            # check if there are any completed projects for the user
            projects = UserCompletedProject.objects.filter(user=self.get_object())
            # check if the user has added skills
            skills = Skill.objects.filter(user=self.get_object())
            if not projects:
                # if there are no projects send a extra form through
                data['UserCompletedProjects'].extra=1
            elif not skills:
                # if there are no skills send a extra form through
                data['SkillsFormset'].extra=1
            data['SkillsFormset']= SkillFormset()
        return data


    
    
    def get_form(self, *args, **kwargs):
        form = super(ProfileView, self).get_form(*args, **kwargs)
        form.fields['full_name'].widget.attrs['class']='circle--input--h1'
        form.fields['full_name'].widget.attrs['placeholder']='Firstname'
        form.fields['full_name'].label=''
        form.fields['bio'].widget.attrs['placeholder']='Tell us about yourself...'
        form.fields['bio'].label=''
        return form 
    
    def form_valid(self, form):
        data = self.get_context_data()
        instance = form.save(commit=False)
        completed_projects = data['UserCompletedProjects']
        skills_formset = data['SkillsFormset']
        if completed_projects.is_valid() and skills_formset.is_valid():
            projects = completed_projects.save(commit=False)
            skills = skills_formset.save(commit=False)
            for project in projects:
                project.user = instance
                project.save()
            for skill in skills:
                skill.user = instance
                skill.save()
            completed_projects.save()
            skills_formset.save()
        instance.save()
            
        return super().form_valid(form)
        
    

        



class loginView(FormView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')


    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

class SignupView(CreateView):
    model = User
    fields = ['display_name','email','password']
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        return super().form_valid(form)


def sign_out(request):
    logout(request)
    messages.success(request, "You've been signed out. Come back soon!")
    return HttpResponseRedirect(reverse('home'))



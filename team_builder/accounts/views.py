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
from projects.forms import ProjectFormSet
from .models import User



class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    success_url = reverse_lazy('home')
    form_class = forms.UserCreateForm
 

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
    
    def get_context_data(self, **kwargs):
        data = super(ProfileView,self).get_context_data(**kwargs)
        if self.request.POST:
            data['projects']= ProjectFormSet(self.request.POST,
                                            instance=self.get_object())
        else:
            data['projects']=ProjectFormSet(instance=self.get_object())
        return data
    
    def form_valid(self, form):
        context = self.get_context_data()
        projects = context['projects']
        if projects.is_valid():
            projects.instance = self.get_object()
            projects.save()
        return super(ProfileView,self).form_valid(form)
    
    def get_form(self, *args, **kwargs):
        form = super(ProfileView, self).get_form(*args, **kwargs)
        form.fields['full_name'].widget.attrs['class']='circle--input--h1'
        form.fields['full_name'].widget.attrs['placeholder']='Firstname'
        form.fields['full_name'].label=''
        form.fields['bio'].widget.attrs['placeholder']='Tell us about yourself...'
        form.fields['bio'].label=''
        return form 
    

        



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



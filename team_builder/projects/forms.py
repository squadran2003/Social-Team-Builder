from django.forms import inlineformset_factory, TextInput
from django.forms import ModelForm
from accounts.models import User
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','url']
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Project Name'}),
            'url': TextInput(
                attrs={'placeholder': 'Project URL'}),
        }

ProjectFormSet = inlineformset_factory(User, 
                                        Project,form=ProjectForm,
                                        max_num=0)
        



from django.forms import BaseModelFormSet
from django.forms import inlineformset_factory, TextInput
from django.forms import ModelForm
from django import forms
from django.forms.models import modelformset_factory
from accounts.models import User

from .models import Project,Position, UserCompletedProject



class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = ('title','description')
    
    def __init__(self,*args, **kwargs):
        super(PositionForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder']='title'
        self.fields['title'].label=''
        self.fields['description'].widget.attrs['placeholder']='description'
        self.fields['description'].label=''


class BasePositionFormset(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(BasePositionFormset, self).__init__(*args, **kwargs)

    def save(self, project_instance):
        instances = super().save(commit=False)
        for instance in instances:
            try:
                """check if a postion exists"""
                exis_pos = Position.objects.get(title=instance.title)
            except Position.DoesNotExist:
                """ if doesnt exists create it and add the relationship"""
                instance.save()
                instance.projects.add(project_instance)
                instance.save()
            else:
                """else just add the relationship not the position"""
                exis_pos.projects.add(project_instance)
                exis_pos.save()
        return super().save(project_instance)






        

PositionFormset = modelformset_factory(Position, form=PositionForm,
                                        extra=0,can_delete=True,formset=BasePositionFormset)

class UserCompletedProjectForm(ModelForm):
    class Meta:
        model = UserCompletedProject
        fields = ('title','url')
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder']='title'
        self.fields['title'].label=''
        self.fields['url'].widget.attrs['placeholder']='enter the url'
        self.fields['url'].label=''

UserCompletedProjectFormset= modelformset_factory(UserCompletedProject, 
                                                        form=UserCompletedProjectForm,
                                                        extra=0,can_delete=True)

    

  





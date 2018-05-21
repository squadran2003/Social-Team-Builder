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


    


        

PositionFormset = modelformset_factory(Position, form=PositionForm,extra=0,can_delete=True)

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

    

  





from django.forms import BaseModelFormSet
from django.forms import ModelForm
from django.contrib import messages
from django.http import request
from django import forms
from django.forms.models import modelformset_factory
from .models import Position, UserCompletedProject


class PositionForm(ModelForm):

    class Meta:
        model = Position
        fields = ('title', 'description', 'skills')

    def __init__(self, *args, **kwargs):
        super(PositionForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = (
                                                'select or enter a position'
                                                )
        self.fields['skills'].label = "Select skills from the list"
        self.fields['title'].widget.attrs['list'] = 'options'
        self.fields['description'].widget.attrs['placeholder'] = 'description'
        self.fields['description'].label = ''


class BasePositionFormset(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(BasePositionFormset, self).__init__(*args, **kwargs)
    
    def clean(self):
        
        if any(self.errors):
            return

        data = super().clean()
        for form in self.forms:
            if form.instance.title == '':
                raise forms.ValidationError("You must enter a position title!",
                                            code='no position title')
            

PositionFormset = modelformset_factory(Position, form=PositionForm,
                                       extra=0, can_delete=True,
                                       formset=BasePositionFormset)


class UserCompletedProjectForm(ModelForm):
    class Meta:
        model = UserCompletedProject
        fields = ('title', 'url')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'title'
        self.fields['title'].label = ''
        self.fields['url'].widget.attrs['placeholder'] = 'enter the url'
        self.fields['url'].label = ''


UserCompletedProjectFormset = modelformset_factory(
                                                UserCompletedProject, 
                                                form=UserCompletedProjectForm,
                                                extra=0, can_delete=True
                                                )

    

  





from django.forms import ModelForm
from django.forms.models import modelformset_factory
from accounts.models import User

from .models import Skill



class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ('name',)
    
    def __init__(self,*args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder']='Your skill'
        self.fields['name'].label=''

        

SkillFormset = modelformset_factory(Skill, form=SkillForm,extra=0,can_delete=True)
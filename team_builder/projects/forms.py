from django.forms import inlineformset_factory, TextInput
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from accounts.models import User

from .models import Project, Position

class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = ('title','description')

ProjectPositionFormset = inlineformset_factory(Project, Position,form=PositionForm,
                                                extra=0)



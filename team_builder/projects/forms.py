from django.forms import inlineformset_factory, TextInput
from django.forms import ModelForm
from django.forms.models import modelformset_factory
from accounts.models import User

from .models import Project,Position


class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = ('title','description')

PositionFormset = modelformset_factory(Position, form=PositionForm,extra=1,can_delete=True)
    





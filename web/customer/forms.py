from django.forms import ModelForm

from .models import *

class EnterForm(ModelForm):
    class Meta:
        model = Enter
        fields = ['is_enter']
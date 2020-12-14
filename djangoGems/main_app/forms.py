from django.forms import ModelForm
from .models import Famous

class FamousForm(ModelForm):
  class Meta:
    model = Famous
    fields = ['name', 'owner', 'ownership']
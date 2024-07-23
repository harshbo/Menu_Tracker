from django.forms import ModelForm
from .models import BreakFast, Lunch, Snacks, Supper


class BreakfastForm(ModelForm):
    class Meta:
        model = BreakFast
        fields = '__all__'

class LunchForm(ModelForm):
  class Meta:
    model=Lunch
    fields='__all__'

class SnacksForm(ModelForm):
  class Meta:
    model=Snacks
    fields='__all__'


class SupperForm(ModelForm):
  class Meta:
    model=Supper
    fields='__all__'


from django.forms import ModelForm
from .models import Exercises,Tracking
from django import forms

class TrackingForm(ModelForm):
  class Meta:
    model = Tracking
    fields = ['date', 'track']

class ExerciseForm(forms.ModelForm):
  class Meta:
    model = Exercises
    fields = ['name', 'sets', 'reps', 'distance', 'yoga_flow']
    widgets = {
    'name': forms.TextInput(attrs={'required': True}),
    'sets': forms.NumberInput(attrs={'required': True}),
    'reps': forms.NumberInput(attrs={'required': True}),
    'distance': forms.NumberInput(attrs={'required': False}),
    'yoga_flow': forms.NumberInput(attrs={'required': False}),
     }
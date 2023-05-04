
from django.forms import ModelForm
from .models import Tracking

class TrackingForm(ModelForm):
  class Meta:
    model = Tracking
    fields = ['date', 'track']
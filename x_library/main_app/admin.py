from django.contrib import admin
# import your models here
from .models import Workout, Exercises

# Register your models here
admin.site.register(Workout)
admin.site.register(Exercises)
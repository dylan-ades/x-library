from django.db import models
from django.urls import reverse
from datetime import date
# Import the User
from django.contrib.auth.models import User

# A tuple of 2-tuples
# TYPE = (
#     ('C', 'Cardio'),
#     ('Y', 'Yoga'),
#     ('S', 'Strength')
# )

class Workout(models.Model):
    workout_type = models.TextField(max_length=150, default='Workout')
    description = models.TextField(max_length=250)
    # Add the foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.workout_type
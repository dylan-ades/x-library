from django.db import models
from django.urls import reverse
from datetime import date
# Import the User
from django.contrib.auth.models import User

# A tuple of 2-tuples
TYPE = (
    ('C', 'Cardio'),
    ('Y', 'Yoga'),
    ('S', 'Strength')
)


# Create your models here.
class Workout(models.Model):
    type = models.CharField(
        max_length=1,
    # add the 'choices' field option
        choices=TYPE,
    # set the default value for workout to be 'C'
        default=TYPE[0][0]
    ),
    description = models.TextField(max_length=250)

    # new code below
    def __str__(self):
        return self.name
        # return f'the horses name is {self.name}'
    
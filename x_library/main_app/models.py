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

    # new code below
    def __str__(self):
        return self.name
        # return f'the horses name is {self.name}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'workout_id': self.id})
    
class Exercises(models.Model):
     name = models.CharField(max_length=100)
     sets = models.IntegerField()
     reps = models.IntegerField()
     distance = models.IntegerField()
     yoga_flow = models.IntegerField()

     def __str__(self):
        return f'{self.name}'
    
     def get_absolute_url(self):
        return reverse('exercises_detail', kwargs={'pk': self.id})
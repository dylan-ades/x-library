from django.db import models
from django.urls import reverse
from datetime import date
# Import the User
from django.contrib.auth.models import User

TRACK = (
    ('C', 'Cardio'),
    ('S', 'Strength'),
    ('Y', 'Yoga')
)

class Exercises(models.Model):
    name = models.CharField(max_length=100)
    sets = models.IntegerField(null=True, blank=True)
    reps = models.IntegerField(null=True, blank=True)
    distance = models.IntegerField(null=True, blank=True)
    yoga_flow = models.CharField(null=True, blank=True)


    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse('exercises_detail', kwargs={'pk': self.id})





class Workout(models.Model):
    workout_type = models.CharField(max_length=150, default='Workout')
    description = models.TextField(max_length=250)
    # Add the foreign key linking to a user instance
    exercises = models.ManyToManyField(Exercises)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    # new code below
    def __str__(self):
        return self.name
        # return f'the horses name is {self.name}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'workout_id': self.id})


class Tracking(models.Model):
    date = models.DateField('workout date')
    track = models.CharField(max_length=5, choices=TRACK, default=TRACK[0][0],)
    
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_track_display()} on {self.date}"

    class Meta:
        ordering = ('-date',)



from django.shortcuts import render, redirect
from django.contrib.auth import login

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# register/signin form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
#Import the mixin for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Workout, Exercises
from .forms import TrackingForm


# A tuple of 2-tuples
# TYPE = (
#     ('C', 'Cardio'),
#     ('Y', 'Yoga'),
#     ('S', 'Strength')
# )

# Add the Workout class & list and view function below the imports
# class Workout:  # Note that parens are optional if not inheriting from another class
#     def __init__(self, type, description):
#         self.type = type
#         self.description = description
    

# workouts = [
#   Workout('C', 'My goal is to do a 6 minute mile today'),
#   Workout('Y', 'May Goal is to loosen my back'),
#   Workout('S', 'My goal is to add 10lbs to my lift'),
# ]

class WorkoutCreate(LoginRequiredMixin, CreateView):
  model = Workout
  fields = ['workout_type', 'description']
  success_url = '/workouts/'
  def form_valid(self, form):
    print('is valid')
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)
  

class WorkoutUpdate(LoginRequiredMixin, UpdateView):
  model = Workout
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['workout_type', 'description']
  

class WorkoutDelete(LoginRequiredMixin, DeleteView):
  model = Workout
  success_url = '/workouts/'


def index(request):
  return render(request, 'index.html')

@login_required
def workouts_index(request):
  workouts = Workout.objects.filter(user=request.user)
  # workouts = Workout.objects.all()
  return render(request, 'workouts/index.html', { 'workouts': workouts })

@login_required
def workouts_detail(request, workout_id):
  workout = Workout.objects.get(id=workout_id)
  # instantiate FeedingForm to be rendered in the template
  exercises_workout_doesnt_have = Exercises.objects.exclude(id__in = workout.exercises.all().values_list('id'))
  # workout.exercises.all().values_list('id')
  tracking_form = TrackingForm()
  return render(request, 'workouts/detail.html', { 
      'workout': workout, 
      'tracking_form' : tracking_form , 
      'exercises': exercises_workout_doesnt_have
    })

@login_required
def add_tracking(request, workout_id):
  form = TrackingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_tracking = form.save(commit=False)
    new_tracking.workout_id = workout_id
    new_tracking.save()
  return redirect('detail', workout_id=workout_id)

@login_required
def assoc_exercise(request, workout_id, exercise_id):
  # Note that you can pass a toy's id instead of the whole object
  Workout.objects.get(id=workout_id).exercises.add(exercise_id)
  return redirect('detail', workout_id=workout_id)


# The purpose of this is to add a specific exercise 
def add_exercise(request, workout_id, exercise_id):
  Workout.objects.get(id=workout_id).exercises.add(exercise_id)
  return redirect('detail', workout_id=workout_id)

# The purpose of this is to remove a specific exercise 
def remove_exercise(request, workout_id, exercise_id):
  Workout.objects.get(id=workout_id).exercises.remove(exercise_id)
  return redirect('detail', workout_id=workout_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('home')
      
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


class ExerciseIndex(LoginRequiredMixin, ListView):
  model = Exercises


class ExerciseDetail(LoginRequiredMixin, DetailView):
  model = Exercises


class ExerciseCreate(LoginRequiredMixin, CreateView):
  model = Exercises
  fields = '__all__'

class ExerciseUpdate(LoginRequiredMixin, UpdateView):
  model = Exercises
  fields = '__all__'

class ExerciseDelete(LoginRequiredMixin, DeleteView):
  model = Exercises
  success_url = '/exercises/'


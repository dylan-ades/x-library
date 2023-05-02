
from django.shortcuts import render
from django.contrib.auth import login
# register/signin form
from django.contrib.auth.forms import UserCreationForm


from .models import Workout

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



def index(request):
  return render(request, 'main_app/index.html')

def workouts_index(request):
  workouts = Workout.objects.filter(user=request.user)
  # workouts = Workout.objects.all()
  return render(request, 'workouts/index.html', { 'workouts': workouts })

# def about(request):
#   return render(request, 'about.html')

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
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)




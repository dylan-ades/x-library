from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='home'),
   path('workouts/', views.workouts_index, name='index'),
   # createView
   path('workouts/create/', views.WorkoutCreate.as_view(), name='workouts_create'),
   # signup
   path('accounts/signup/', views.signup, name='signup'),
]
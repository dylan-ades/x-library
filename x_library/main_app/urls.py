from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='home'),
   path('workouts/', views.workouts_index, name='index'),
   # createView
   path('workouts/create/', views.WorkoutCreate.as_view(), name='workouts_create'),
   # updateView
   path('workouts/<int:pk>/update/', views.WorkoutUpdate.as_view(), name='workouts_update'),
   # deleteView
   path('workouts/<int:pk>/delete/', views.WorkoutDelete.as_view(), name='workouts_delete'),
   # signup
   path('accounts/signup/', views.signup, name='signup'),
]
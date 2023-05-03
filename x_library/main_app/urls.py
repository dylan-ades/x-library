from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='home'),
   path('workouts/', views.workouts_index, name='index'),
   path('workouts/<int:workout_id>/', views.workouts_detail, name='detail'),
   # createView
   # path('workouts/create/', views.WorkoutCreate.as_view(), name='workouts_create'),
   # # updateView
   # path('workouts/<int:pk>/update/', views.WorkoutUpdate.as_view(), name='workouts_update'),
   # deleteView
   path('workouts/<int:pk>/delete/', views.WorkoutDelete.as_view(), name='workouts_delete'),
   # signup
   path('accounts/signup/', views.signup, name='signup'),
   # 
  
   path('exercises/create/', views.ExerciseCreate.as_view(), name='exercises_create'),
   path('exercises/', views.ExerciseIndex.as_view(), name='exercises_index'),
   path('exercises/<int:pk>/', views.ExerciseDetail.as_view(), name='exercises_detail'),
   path('exercises/<int:pk>/update/', views.ExerciseUpdate.as_view(), name='exercises_update'),
   path('exercises/<int:pk>/delete/', views.ExerciseDelete.as_view(), name='exercises_delete'),
]
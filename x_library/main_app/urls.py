from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   # New url pattern below
   path('accounts/signup/', views.signup, name='signup'),
]
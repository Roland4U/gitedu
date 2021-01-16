from django.urls import path
from .views import *

urlpatterns = [
    path('facultets', FacultetListAPIView.as_view()),
    path('trainings', TrainingListAPIView.as_view()),
    path('services', ServiceListAPIView.as_view()),
    path('facultets/<str:slug>', FacultetDetailAPIView.as_view()),
    path('trainings/<str:slug>', TrainingDetailAPIView.as_view()),
    path('services/<str:slug>', ServiceDetailAPIView.as_view()),
]

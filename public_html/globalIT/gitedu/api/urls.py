from django.urls import path, include
from .views import *

urlpatterns = [
    path('v1/facultets', FacultetListAPIView.as_view()),
    path('v1/trainings', TrainingListAPIView.as_view()),
    path('v1/services', ServiceListAPIView.as_view()),
    path('v1/facultets/<str:slug>', FacultetDetailAPIView.as_view()),
    path('v1/trainings/<str:slug>', TrainingDetailAPIView.as_view()),
    path('v1/services/<str:slug>', ServiceDetailAPIView.as_view()),
    path('v1/api-auth/', include('rest_framework.urls')),
    path('v1/auth/', include('djoser.urls')),
    path('v1/auth/', include('djoser.urls.authtoken')),
    path('v1/auth/', include('djoser.urls.jwt')),
]

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from ..models import *

class FacultetListAPIView(APIView):

    def get(self, request):
        facultets = facultet.objects.order_by('id')
        serializer = FacultetSerializer(facultets, many=True)
        return Response(serializer.data)

class TrainingListAPIView(APIView):

    def get(self, request):
        trainings = training.objects.all()
        serializer = TrainingSerializer(trainings, many=True)
        return Response(serializer.data)

class ServiceListAPIView(APIView):

    def get(self, request):
        services = service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

class FacultetDetailAPIView(APIView):

    def get(self, request, slug):
        facultets = facultet.objects.get(slug__iexact=slug)
        serializer = FacultetSerializer(facultets)
        return Response(serializer.data)

class TrainingDetailAPIView(APIView):

    def get(self, request, slug):
        trainings = training.objects.get(slug__iexact=slug)
        serializer = TrainingSerializer(trainings)
        return Response(serializer.data)

class ServiceDetailAPIView(APIView):

    def get(self, request, slug):
        services = service.objects.get(slug__iexact=slug)
        serializer = ServiceSerializer(services)
        return Response(serializer.data)


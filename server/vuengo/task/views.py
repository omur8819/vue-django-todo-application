from django.shortcuts import render

from .models import Task
from .serializers import TaskSerializer

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics

# class TaskViewSet(viewsets.ModelViewSet):
#     authentication_classes = (BasicAuthentication,)
#     permission_classes = Task.objects.all()
#     serializer_class = TaskSerializer


class TaskView(generics.RetrieveAPIView):
    queryset = Task.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        Task.objects.create(**data)
        return Response({ 'status': True })

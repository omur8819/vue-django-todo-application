from django.db.models import F
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task
from api.swagger_schemas.Task import TaskParams
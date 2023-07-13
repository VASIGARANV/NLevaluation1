from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import App
from .serializers import AppSerializer
# Create your views here.

class AppViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = App.objects.all()
    serializer_class = AppSerializer
    # permission_classes = [permissions.IsAuthenticated]
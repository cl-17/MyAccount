import django_filters
from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Classification
from .serializer import ClassificationSerializer

# Create your views here.
def master(request):
    return render(request, 'master.html')

def list(request, master):
    return render(request, 'list.html')

def maintenance(request, master):
    return render(request, 'maintenance.html')

class ClassificationViewSet(viewsets.ModelViewSet):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer




from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Issue
from .serializers import IssueSerializer

# List all issues or create new one
class IssueListCreateAPIView(generics.ListCreateAPIView):
    queryset = Issue.objects.all().order_by('-created_at')
    serializer_class = IssueSerializer

# Retrieve, update, delete a single issue
class IssueDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
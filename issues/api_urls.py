from django.urls import path
from .views import IssueListCreateAPIView, IssueDetailAPIView

urlpatterns = [
    path('issues/', IssueListCreateAPIView.as_view(), name='issue-list-create'),
    path('issues/<int:pk>/', IssueDetailAPIView.as_view(), name='issue-detail'),
]

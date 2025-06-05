from rest_framework import generics, status
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    """
    GET /api/tasks/ — Return all tasks
    POST /api/tasks/ — Add a new task
    """
    queryset = Task.objects.all().order_by('-created_at') # Show newest first
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET /api/tasks/:id/ — Retrieve a specific task
    PUT /api/tasks/:id/ — Mark as completed (or update other fields)
    DELETE /api/tasks/:id/ — Delete a task
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
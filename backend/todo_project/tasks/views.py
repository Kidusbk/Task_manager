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
        # The requirement "Mark as completed" for PUT implies only 'completed' should change.
        # A standard PUT replaces the entire resource. PATCH is for partial updates.
        # We'll interpret "Mark as completed" via PUT to mean updating the task,
        # where 'completed' is one of the fields that can be set.
        # If the client sends `{"completed": true}`, it will work.
        # If they send `{"title": "new", "completed": true}`, that also works.

        # If you strictly want PUT to *only* modify 'completed':
        # partial = kwargs.pop('partial', False) # Standard DRF way
        # instance = self.get_object()
        # data_to_update = {'completed': request.data.get('completed', instance.completed)}
        # if 'completed' not in request.data:
        #     return Response({"detail": "The 'completed' field is required for this PUT request."},
        #                     status=status.HTTP_400_BAD_REQUEST)

        # serializer = self.get_serializer(instance, data=data_to_update, partial=partial) # Use partial=True to allow only one field
        # serializer.is_valid(raise_exception=True)
        # self.perform_update(serializer)
        # return Response(serializer.data)

        # For simplicity and common DRF usage, we'll stick to default PUT behavior.
        # The client can send a payload like {"completed": true} or {"title": "updated", "completed": true}
        return super().update(request, *args, **kwargs)
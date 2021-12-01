from .models import Task
from rest_framework import viewsets
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TaskSerializer
from django.core import serializers
from .models import Task


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")


@api_view(['DELETE'])
def delete_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    task.delete()
    return HttpResponse("Task deletada com sucesso", status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def get_or_post(request):

    if request.method == 'GET':
        get_task = Task.objects.all()
        serializer_json = serializers.serialize("json", get_task)
        return HttpResponse(serializer_json, content_type="application/json", status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

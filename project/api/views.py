from rest_framework.request import Request
from rest_framework.response import Response
from todo.models import Task
from rest_framework import status
from .serialaziers import TaskSerializer
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


class TaskViewSet(viewsets.ViewSet):
    def list(self, request: Request) -> Response:
        tasks = Task.objects.all()
        tasks_serializer = TaskSerializer(tasks, many=True)
        return Response(tasks_serializer.data)

    def create(self, request: Request) -> Response:
        tasks_serializer_from_request = TaskSerializer(data=request.data)
        if tasks_serializer_from_request.is_valid():
            tasks_serializer_from_request.save()
        return Response(status=status.HTTP_201_CREATED)

    def retrieve(self, request: Request, pk: int = None) -> Response:
        task = get_object_or_404(Task, pk=pk)
        if isinstance(task, Response):
            return task

        tasks_serializer = TaskSerializer(task)
        return Response(tasks_serializer.data)

    def update(self, request: Request, pk: int = None) -> Response:
        task = get_object_or_404(Task, pk=pk)
        tasks_serializer_from_request = TaskSerializer(task, data=request.data)
        if tasks_serializer_from_request.is_valid():
            tasks_serializer_from_request.save()
            return Response(status=status.HTTP_200_OK)

        return Response(tasks_serializer_from_request.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request: Request, pk: int = None) -> Response:
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from typing import Union
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from todo.models import Task
from rest_framework import status
from .serialaziers import TaskSerializer


def get_task_or_return_404(task_id: int) -> Union[Task, Response]:
    try:
        return Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_tasks(request: Request) -> Response:
    tasks = Task.objects.all()
    tasks_serializer = TaskSerializer(tasks, many=True)
    return Response(tasks_serializer.data)


@api_view(['POST'])
def create_task(request: Request) -> Response:
    tasks_serializer_from_request = TaskSerializer(data=request.data)
    if tasks_serializer_from_request.is_valid():
        tasks_serializer_from_request.save()
    return Response(tasks_serializer_from_request.data)


@api_view(['PUT'])
def update_task(request: Request, task_id: int) -> Response:
    task = get_task_or_return_404(task_id)
    if isinstance(task, Response):
        return task

    tasks_serializer_from_request = TaskSerializer(task, data=request.data)
    if tasks_serializer_from_request.is_valid():
        tasks_serializer_from_request.save()
        return Response(tasks_serializer_from_request.data)

    return Response(tasks_serializer_from_request.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_task(request: Request, task_id: int) -> Response:
    task = get_task_or_return_404(task_id)
    if isinstance(task, Response):
        return task

    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

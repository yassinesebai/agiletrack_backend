from django.shortcuts import render
from .models import Project, Task, Sprint
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProjectSerializer, EmployeeSerializer, TaskSerializer, SprintListSerializer
from django.contrib.auth import get_user_model
from rest_framework import status

@api_view(['GET'])
def get_users(request):
    emps = get_user_model().objects.all()
    emps = EmployeeSerializer(emps, many=True)
    return Response(emps.data)

@api_view(['GET'])
def get_projects(request):
    projects = Project.objects.all()
    projects_ser = ProjectSerializer(projects, many=True)
    return Response(projects_ser.data)

@api_view(['GET'])
def get_project(request, id):
    try:
        project = Project.objects.get(id=id)
        project_ser = ProjectSerializer(project, many=False)
        return Response(project_ser.data)
    except Project.DoesNotExist:
        return Response({'message': 'The project does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_latest_tasks(request, id):
    latest_tasks = Task.objects.filter(project_id=id).order_by('-id')[:5]
    latest_tasks_ser = TaskSerializer(latest_tasks, many=True)
    return Response(latest_tasks_ser.data)

@api_view(['GET'])
def get_backlogTasks(request, id):
    tasks = Task.objects.filter(project_id=id, sprint__isnull=True).order_by('id')
    tasks_ser = TaskSerializer(tasks, many=True)
    return Response(tasks_ser.data)

@api_view(['GET'])
def get_sprintList(request, id):
    sprints = Sprint.objects.filter(project_id=id).exclude(status="completed")
    sprints_ser = SprintListSerializer(sprints, many=True)
    return Response(sprints_ser.data)

@api_view(['POST'])
def add_task(request):
    task_ser = TaskSerializer(data=request.data)
    if task_ser.is_valid():
        task_ser.save()
    else:
        print(task_ser.errors)
    return Response(task_ser.data)

@api_view(['PUT'])
def update_task(request):
    task_data = request.data
    task = Task.objects.get(id=task_data['id'])
    serializer = TaskSerializer(task, data=task_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['DELETE'])
def delete_task(request, id):
    try:
        task = Task.objects.get(pk=id)
    except Task.DoesNotExist:
        return Response({'message': 'Task does not exist !'}, status=status.HTTP_404_NOT_FOUND)
    task.delete()
    return Response({'message': 'Task deleted successfully'})
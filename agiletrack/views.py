from django.shortcuts import render

from accounts.serializers import UserSerializer
from .models import Project, Task, Sprint, Job
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from .serializers import ProjectSerializer, EmployeeSerializer, JobSerializer, TaskSerializer, SprintListSerializer, SprintSerializer
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.parsers import MultiPartParser

@api_view(['GET'])
def get_employees(request):
    emps = get_user_model().objects.all()
    emps = EmployeeSerializer(emps, many=True)
    return Response(emps.data)

@api_view(['GET'])
def get_employee(request, id):
    try:
        user = get_user_model().objects.get(id=id)
        print(user.username)
        user_serializer = UserSerializer(user, many=False)
        return Response(user_serializer.data)
    except get_user_model().DoesNotExist:
        return Response({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_employee(request):
    user = get_user_model().objects.get(id=request.data['id'])
    data = request.data
    data.pop('image')
    if data['password'] == "":
        data.pop('password')
        data.pop('password2')
    serializer = UserSerializer(user, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        print(serializer.errors)
        return Response(serializer.errors)

@api_view(['PUT'])
@parser_classes([MultiPartParser])
def update_employee_image(request, id):
    user = get_user_model().objects.get(id=id)
    print(request.FILES['image'])
    user.image = request.FILES['image']
    user.save()
    return Response("h")
    #user.image = request.FILES
    #print(request.data.pop('image'))
    # serializer = UserSerializer(user, data=request.data)
    # if serializer.is_valid():
    #     serializer.save()
    #     return Response(serializer.data)
    # else:
    #     return Response(serializer.errors)

@api_view(['GET'])
def get_projects(request):
    projects = Project.objects.all().order_by('id')
    projects_ser = ProjectSerializer(projects, many=True)
    return Response(projects_ser.data)

@api_view(['GET'])
def get_user_projects(request, id):
    user = get_user_model().objects.get(id=id)
    projects = Project.objects.filter(employee=user)
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

@api_view(['POST'])
def add_project(request):
    project_ser = ProjectSerializer(data=request.data)
    if project_ser.is_valid():
        project_ser.save()
        return Response(project_ser.data)
    else:
        print(project_ser.errors)
        return Response(project_ser.errors)    

@api_view(['PUT'])
def update_project(request):
    project_data = request.data
    project = Project.objects.get(id=project_data['id'])
    serializer = ProjectSerializer(project, data=project_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['DELETE'])
def delete_project(request, id):
    try:
        project = Project.objects.get(pk=id)
    except Project.DoesNotExist:
        return Response({'message': 'Project does not exist !'}, status=status.HTTP_404_NOT_FOUND)
    project.delete()
    return Response({'message': 'Project deleted successfully'})

@api_view(['GET'])
def get_latest_tasks(request, id):
    latest_tasks = Task.objects.filter(project_id=id).order_by('-id')[:5]
    latest_tasks_ser = TaskSerializer(latest_tasks, many=True)
    return Response(latest_tasks_ser.data)

@api_view(['GET'])
def get_team_members(request, id):
    project = Project.objects.get(id=id)
    team = project.employees
    team_ser = EmployeeSerializer(team, many=True)
    return Response(team_ser.data)

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
        return Response(task_ser.data)
    else:
        print(task_ser.errors)
        return Response(task_ser.errors)

@api_view(['PUT'])
def update_task(request):
    task_data = request.data
    task = Task.objects.get(id=task_data['id'])
    serializer = TaskSerializer(task, data=task_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        print(serializer.errors)
        return Response(serializer.errors)

@api_view(['DELETE'])
def delete_task(request, id):
    try:
        task = Task.objects.get(pk=id)
    except Task.DoesNotExist:
        return Response({'message': 'Task does not exist !'}, status=status.HTTP_404_NOT_FOUND)
    task.delete()
    return Response({'message': 'Task deleted successfully'})

@api_view(['GET'])
def get_sprints(request, id):
    sprints = Sprint.objects.filter(project_id=id)
    sprints_ser = SprintSerializer(sprints, many=True)
    return Response(sprints_ser.data)

@api_view(['GET'])
def get_active_sprint(request, id):
    try:
        active_sprint = Sprint.objects.get(project_id=id, status="inprogress")
        return Response(active_sprint.id)
    except Sprint.DoesNotExist:
        return Response(None)

@api_view(['GET'])
def get_sprint_tasks(request, id):
    sprint_tasks = Task.objects.filter(sprint_id=id).order_by('id')
    sprint_tasks_ser = TaskSerializer(sprint_tasks, many=True)
    return Response(sprint_tasks_ser.data)

@api_view(['POST'])
def add_sprint(request):
    sprint_ser = SprintSerializer(data=request.data)
    if sprint_ser.is_valid():
        sprint_ser.save()
        return Response(sprint_ser.data)
    else:
        print(sprint_ser.errors)
        return Response(sprint_ser.errors)

@api_view(['PUT'])
def update_sprint(request):
    sprint_data = request.data
    sprint = Sprint.objects.get(id=sprint_data['id'])
    serializer = SprintSerializer(sprint, data=sprint_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['DELETE'])
def delete_sprint(request, id):
    try:
        sprint = Sprint.objects.get(pk=id)
    except Sprint.DoesNotExist:
        return Response({'message': 'Sprint does not exist !'}, status=status.HTTP_404_NOT_FOUND)
    sprint.delete()
    return Response({'message': 'Sprint deleted successfully'})

@api_view(['GET'])
def get_jobs(request):
    jobs = Job.objects.all()
    jobs_serializer = JobSerializer(jobs, many=True)
    return Response(jobs_serializer.data)
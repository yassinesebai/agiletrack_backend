import datetime
from rest_framework import serializers
from .models import Project, Task, Sprint
from django.contrib.auth import get_user_model

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'password', 'image', 'groups']

class ProjectSerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True)
    progress = serializers.SerializerMethodField()
    done_tasks = serializers.SerializerMethodField()
    total_tasks = serializers.SerializerMethodField()
    remaining_days = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    def get_progress(self, obj):
        total_tasks = Task.objects.filter(project=obj).count()
        done_tasks = Task.objects.filter(project=obj, status='done').count()
        if total_tasks > 0:
            return (done_tasks / total_tasks) * 100
        return 0

    def get_done_tasks(self, obj):
        return Task.objects.filter(project=obj, status='done').count()

    def get_total_tasks(self, obj):
        return Task.objects.filter(project=obj).count()

    def get_remaining_days(self, obj):
        estimated_end_date = obj.estimated_end_date
        today = datetime.date.today()
        return (estimated_end_date - today).days

class TaskSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(many=False, required=False, allow_null=True, )
    class Meta:
        model = Task
        fields = '__all__'

    def to_internal_value(self, data):
        employee_id = data.pop('employee', None)
        print(employee_id)
        instance = super().to_internal_value(data)
        if employee_id:
            employee = get_user_model().objects.get(id=employee_id)
            instance['employee'] = employee
        else:
            instance['employee'] = None
        print(instance)
        return instance
    
class SprintListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = ['id', 'name']

class SprintSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()

    def get_tasks(self, obj):
        tasks = obj.task_set.all()
        task_serializer = TaskSerializer(tasks, many=True)
        return task_serializer.data
    class Meta:
        model = Sprint
        fields = '__all__'
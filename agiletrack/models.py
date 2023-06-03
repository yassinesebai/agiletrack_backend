from django.contrib.auth import get_user_model
from django.db import models
import datetime

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    start_date = models.DateField()
    estimated_end_date = models.DateField()
    end_date = models.DateField(null=True)
    is_completed = models.BooleanField(default=False)
    estimated_duration = models.IntegerField()
    duration = models.IntegerField(null=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    employees = models.ManyToManyField(get_user_model(), through='agiletrack.Team')

    @property
    def cost(self):
        tasks = Task.objects.filter(project=self)
        cost = 0
        for t in tasks:
            cost += t.cost
        return cost

    def delete(self, *args, **kwargs):
        # Delete associated Team entries
        Team.objects.filter(project=self).delete()
        super().delete(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.pk:
            self.start_date = datetime.date.today()
            d_duration = self.estimated_end_date - self.start_date
            self.estimated_duration = d_duration.days

    def complete_project(self):
        self.end_date = datetime.date.today()
        self.is_completed = True
        self.duration = (self.end_date - self.start_date).days
    
class Job(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

class Sprint(models.Model):
    name = models.CharField(max_length=200)
    goal = models.CharField(max_length=250)
    start_date = models.DateField(null=True)
    estimated_end_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    estimated_duration = models.IntegerField(null=True)
    duration = models.IntegerField(null=True)
    status = models.CharField(max_length=20, default="todo")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Task(models.Model):
    summary = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    duration = models.IntegerField(null=True)
    status = models.CharField(max_length=20, default="todo")
    priority = models.CharField(max_length=20)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    employee = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class Team(models.Model):
    employee = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
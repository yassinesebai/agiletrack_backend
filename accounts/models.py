from django.db import models
from django.contrib.auth.models import AbstractUser

class Employee(AbstractUser):
    image = models.ImageField(upload_to='', blank=True, null=True)
    job = models.ForeignKey('agiletrack.Job', on_delete=models.CASCADE, null=True)
    projects = models.ManyToManyField('agiletrack.Project', through='agiletrack.Team')
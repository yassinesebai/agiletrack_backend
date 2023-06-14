from django.db import models
from django.contrib.auth.models import AbstractUser, Group

class Employee(AbstractUser):
    image = models.ImageField(upload_to='', blank=True, null=True, default='default.jpg')
    job = models.ForeignKey('agiletrack.Job', on_delete=models.CASCADE, blank=True, null=True)
    projects = models.ManyToManyField('agiletrack.Project', through='agiletrack.Team')

    REQUIRED_FIELDS= ['email', 'first_name', 'last_name', 'email', 'password']
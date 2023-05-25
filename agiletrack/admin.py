from django.contrib import admin
from .models import Project, Sprint, Task, Team, Job

# Register your models here.
admin.site.register(Project)
admin.site.register(Sprint)
admin.site.register(Task)
admin.site.register(Team)
admin.site.register(Job)
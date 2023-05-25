from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('projects/', views.get_projects, name="get_projects"),
    path('project/<int:id>', views.get_project, name="get_project"),
    path('project/<int:id>/latest_tasks', views.get_latest_tasks, name="get_latest_tasks_"),
    path('project/<int:id>/backlog', views.get_backlogTasks, name="get_backlogTasks"),
    path('project/<int:id>/sprints_list', views.get_sprintList, name="get_sprintList"),
    path('project/<int:id>/add', views.add_task, name="add_task"), 
    path('users/', views.get_users, name="get_users"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
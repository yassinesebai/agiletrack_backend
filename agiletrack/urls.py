from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('projects/', views.get_projects, name="get_projects"),
    path('project/<int:id>', views.get_project, name="get_project"),
    path('project/<int:id>/latest_tasks', views.get_latest_tasks, name="get_latest_tasks_"),
    path("project/<int:id>/team_members", views.get_team_members, name="get_team_members"),
    path('project/<int:id>/backlog', views.get_backlogTasks, name="get_backlogTasks"),
    path('project/<int:id>/sprints_list', views.get_sprintList, name="get_sprintList"),
    path('project/tasks/add', views.add_task, name="add_task"), 
    path('project/tasks/update', views.update_task, name="update_task"),
    path('project/tasks/<int:id>/delete', views.delete_task, name="delete_task"),
    path('project/<int:id>/sprints', views.get_sprints, name="get_sprints"),
    path('sprint/<int:id>/tasks', views.get_sprint_tasks, name="get_sprint_tasks"),
    path('project/sprints/add', views.add_sprint, name="add_sprint"), 
    path('project/sprints/update', views.update_sprint, name="update_sprint"),
    path('project/sprints/<int:id>/delete', views.delete_sprint, name="delete_sprint"),

    path('users/', views.get_users, name="get_users"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
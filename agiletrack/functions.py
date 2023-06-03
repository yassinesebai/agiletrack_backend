from .models import Project

def updatePorjectCost(id, cost):
    project = Project.objects.get(id=id)
    project.cost += cost
    project.save()
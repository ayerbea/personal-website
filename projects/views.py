from django.shortcuts import render
from .helpers import fill_projects
from .models import Project

def projects_view(request):
    fill_projects()
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects.html', context)
# Create your views here.

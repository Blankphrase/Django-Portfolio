from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Project

# Create your views here.
def projects(request):
    projects = Project.all_projects()

    return render(request, 'project.html', {"projects": projects})
    
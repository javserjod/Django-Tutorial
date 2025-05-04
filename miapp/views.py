#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render


# Create your views here.
def index(request):
    title = "Mi primera app con Django!"
    return render(request, 'index.html', {'title': title})


def about(request):
    username = 'Javier'
    return render(request, 'about.html', {'username': username})    


def hello(request, username):
    return HttpResponse(f"<h1>Hello, {username}</h1>")


def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()    # devuelve todos los objetos de la tabla Project
    
    return render(request, 'projects.html', {'projects': projects})    # renderiza el template projects.html y le pasa la variable projects

def tasks(request):
    #task = get_object_or_404(Task, id=id)    # devuelve un 404 si no encuentra el objeto
    return render(request, 'tasks.html')
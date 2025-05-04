#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTaskForm, CreateNewProjectForm

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
    
    return render(request, 'projects/projects.html', {'projects': projects})    # renderiza el template projects.html y le pasa la variable projects

def tasks(request):
    #task = get_object_or_404(Task, id=id)    # devuelve un 404 si no encuentra el objeto
    tasks = Task.objects.all()    # devuelve todos los objetos de la tabla Task
    return render(request, 'tasks/tasks.html', {'tasks': tasks})    # renderiza el template tasks.html y le pasa la variable tasks


def create_task(request):
    if request.method == 'GET':
        #show interface
        return render(request, 'tasks/create_task.html', {'form': CreateNewTaskForm})    # renderiza el template create_task.html
    else:
        # create new task
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=1)    # crea una nueva tarea con los datos del formulario
        return redirect('/tasks/')   # redirige a la vista de tareas

def create_project(request):
    if request.method == 'GET':
        #show interface
        return render(request, 'projects/create_project.html', {'form': CreateNewProjectForm})    # renderiza el template create_project.html
    else:
        #create new project
        Project.objects.create(name=request.POST['name'])
        
        #show interface
        return render(request, 'projects/create_project.html', {'form': CreateNewProjectForm})    # renderiza el template create_project.html
from django.db import models

# Create your models here.
class Project(models.Model):    # equivale a tabla
    name = models.CharField(max_length=200)
    
    def __str__(self):    # devuelve el nombre del proyecto como string
        return self.name
    


class Task(models.Model):    # equivale a tabla
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)    # clave foranea. Si se borra el proyecto, se borran las tareas asociadas en cascada
    
    def __str__(self):    # devuelve el titulo de la task como string
        return self.title+ " - " + self.project.name    # devuelve el titulo de la tarea y el nombre del proyecto asociado
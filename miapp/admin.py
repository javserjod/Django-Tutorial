from django.contrib import admin
from .models import Project, Task

# Register your models here.
admin.site.register(Project)    # registrar el modelo Project en el admin
admin.site.register(Task)    # registrar el modelo Task en el admin
from django import forms


class CreateNewTaskForm(forms.Form):
    title = forms.CharField(label='Título de la tarea', max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'input'}), label='Descripción de la tarea')


class CreateNewProjectForm(forms.Form):
    name = forms.CharField(label='Nombre del proyecto', max_length=200, required=True, widget = forms.TextInput(attrs={'class': 'input'}))
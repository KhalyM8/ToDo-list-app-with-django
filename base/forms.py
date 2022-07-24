from django.forms import ModelForm
from .models import Task, Workspace

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

class WorkspaceForm(ModelForm):
    class Meta:
        model = Workspace
        fields = "__all__"
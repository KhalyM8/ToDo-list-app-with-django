from django.shortcuts import render, redirect
from .models import Task, Workspace
from .forms import TaskForm, WorkspaceForm

# Create your views here.

def home(request):
    workspaces = Workspace.objects.all()
    context = {"workspaces":workspaces}

    return render(request, "base/home.html", context)

def task(request, pk):
    task=Task.objects.get(id=pk)
    context = {"task" : task}

    return render(request, "base/task.html", context)

def createTask(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "base/todo_forum.html", context)

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == "POST":
        task.delete()
        return redirect("home")

    return render(request, "base/delete.html", {"obj":task})

def workspace(request, pk):
    tasks = Task.objects.filter(workspace=pk)
    workspace = Workspace.objects.get(id=pk)
    context = {"tasks":tasks, "workspace":workspace}

    return render(request, "base/workspaces.html", context)

def createWorkpace(request):
    form = WorkspaceForm()
    if request.method == "POST":
        form = WorkspaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "base/todo_forum.html", context)

def deleteWorkspace(request, pk):
    workspace = Workspace.objects.get(id=pk)
    if request.method == "POST":
        workspace.delete()
        return redirect("home")

    return render(request, "base/delete.html", {"obj":workspace})

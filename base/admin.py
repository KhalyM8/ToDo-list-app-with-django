from django.contrib import admin
from .models import Task, Workspace

# Register your models here.

admin.site.register(Task)
admin.site.register(Workspace)
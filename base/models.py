from django.db import models

# Create your models here.

class Workspace(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.name



class Task(models.Model):
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    description = models.CharField(null=True, max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.name


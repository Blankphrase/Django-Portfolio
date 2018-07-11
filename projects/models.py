from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    live_link = models.CharField(max_length=250)
    github_link = models.CharField(max_length = 250)
    screenshot = models.ImageField(upload_to = 'projects/')

    @classmethod
    def all_projects(cls):
        projects = cls.objects.all()
        return projects
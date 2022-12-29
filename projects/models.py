from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tools_used = models.TextField()
    img_name = models.CharField(max_length=30)
    created = models.BooleanField(default=False)

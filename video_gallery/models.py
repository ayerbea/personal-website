from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_id = models.CharField(max_length=30)
# Create your models here.

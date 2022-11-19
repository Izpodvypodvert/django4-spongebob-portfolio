from django.db import models
from django.utils import timezone


class Blog(models.Model):

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/images/')
    url = models.URLField(blank=True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

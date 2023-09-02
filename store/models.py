from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description=models.TextField()
    publish_date = models.DateField(auto_now_add=True)
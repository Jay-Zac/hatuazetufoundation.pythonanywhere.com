from django.db import models


class Logo(models.Model):
    objects = None
    image = models.ImageField(upload_to='logos')


class Blog(models.Model):
    objects = None
    title = models.CharField(max_length=500)
    content = models.TextField()
    thumbnail_url = models.CharField(max_length=2083)
    
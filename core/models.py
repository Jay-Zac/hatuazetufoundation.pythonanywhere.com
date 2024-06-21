from django.db import models


class Blog(models.Model):
    objects = None
    title = models.CharField(max_length=500)
    content = models.TextField()
    thumbnail_url = models.CharField(max_length=2083)


class UserComment(models.Model):
    objects = None
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()



from django.db import models

class Poll(models.Model):
    name = models.SlugField(max_length=30, unique=True)
    password = models.CharField(max_length=255, blank=True)
    poll_jsonstring = models.TextField(null=True, blank=True)
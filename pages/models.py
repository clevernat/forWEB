from django.db import models
from datetime import datetime
import uuid
from tinymce.models import HTMLField

# Create your models here.


class WhatWeDo(models.Model):
    description = models.CharField(max_length=6000)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.description)


class Moderator(models.Model):
    name = models.CharField(max_length=200)
    school = models.CharField(max_length=500)
    occupation = models.CharField(max_length=500)
    location = models.CharField(max_length=200)
    is_staff = models.BooleanField(default=False)
    featured_image = models.ImageField(
        null=True, upload_to='five-students/', default="five-students/default.jpg")
    description = HTMLField(null=True, blank=True)
    social_email = models.EmailField(max_length=200, null=True, blank=True)
    social_facebook = models.URLField(max_length=2048, null=True, blank=True)
    social_linkedin = models.URLField(max_length=2048, null=True, blank=True)
    social_github = models.URLField(max_length=2048, null=True, blank=True)
    social_youtube = models.URLField(max_length=2048, null=True, blank=True)
    social_instagram = models.URLField(max_length=2048, null=True, blank=True)
    social_snapchat = models.URLField(max_length=2048, null=True, blank=True)
    social_website = models.URLField(max_length=2048, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name

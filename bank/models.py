from django.db import models
from django_resized import ResizedImageField
from django.urls import reverse

# Create your models here.
class Bank(models.Model):
    name = models.CharField(max_length=100)
    services = models.TextField()
    logo = models.ImageField(upload_to='images/', null=True)
    link = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
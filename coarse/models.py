from django.db import models
from django_resized import ResizedImageField
from django.urls import reverse
from app.storage_backend import PublicMediaStorage

# Create your models here.
class Coarse(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(storage=PublicMediaStorage(), null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    
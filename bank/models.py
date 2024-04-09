from django.db import models
from django_resized import ResizedImageField
from django.urls import reverse
from app.storage_backend import PublicMediaStorage


class FinancialServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    desscription = models.TextField()

    def __str__(self):
        return self.name
    
# Create your models here.
class Bank(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(FinancialServiceCategory, on_delete=models.CASCADE,null=True)
    services = models.TextField()
    logo = models.ImageField(storage=PublicMediaStorage(), null=True,blank=True)
    link = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
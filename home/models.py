from django.db import models
from app.storage_backend import PublicMediaStorage


class SiteDetails(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(storage=PublicMediaStorage(), null=True,blank=True)
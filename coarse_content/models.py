from django.db import models
from coarse.models import Coarse
from martor.models import MartorField
from app.storage_backend import PublicMediaStorage

# Create your models here.
class CoarseContent(models.Model):
    name = models.CharField(max_length=100)
    notes = MartorField()
    video = models.FileField(storage=PublicMediaStorage(), null=True)
    coarse = models.ForeignKey(Coarse,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
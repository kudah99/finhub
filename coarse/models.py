from django.db import models
from django_resized import ResizedImageField
from django.urls import reverse

# Create your models here.
class Coarse(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = ResizedImageField(size=[500, 500], upload_to='images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("coarse", kwargs={"id": self.pk})
    
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.TextField(null=False, blank=False)
    file = models.FileField(null=True)
    image_preview = models.ImageField(null=False)
    
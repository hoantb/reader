from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.TextField(null=False, blank=False)
    file = models.FileField(null=True, blank=True, upload_to='books')
    image_preview = models.ImageField(null=True, blank=True,upload_to='books')
    
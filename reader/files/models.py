from django.db import models
from books.models import Book


class File(models.Model):
    title = models.TextField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(null=True, blank=True, upload_to='files')
    image_preview = models.ImageField(null=True, blank=True,upload_to='files')
    book = models.ForeignKey(Book, null=True, blank=True, on_delete=models.SET_NULL, related_name='files')
    
    def __str__(self):
        return self.title 
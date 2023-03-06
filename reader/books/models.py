from django.db import models
from categories.models import BookCategory

class Book(models.Model):
    title = models.TextField(null=False, blank=False)
    image_preview = models.ImageField(null=True, blank=True,upload_to='books')
    description = models.TextField(null=True, blank=True)
    total_views = models.IntegerField(null=True, default=0)
    date_created = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(BookCategory, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

class BookUpcoming(models.Model):
    title = models.TextField(null=False, blank=False)
    image_preview = models.ImageField(null=True, blank=True,upload_to='books')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
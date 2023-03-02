from django.db import models


class Book(models.Model):
    title = models.TextField(null=False, blank=False)
    image_preview = models.ImageField(null=True, blank=True,upload_to='books')
    description = models.TextField(null=True, blank=True)
    total_views = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.title
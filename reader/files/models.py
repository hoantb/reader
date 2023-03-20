from django.db import models
from books.models import Book


class File(models.Model):
    def upload_episode(instance, file_name):
        return instance.book.storage_name + "/" + instance.storage_name + "/" + file_name

    title = models.TextField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(null=True, blank=True, upload_to=upload_episode)
    image_preview = models.ImageField(null=True, blank=True, upload_to=upload_episode)
    book = models.ForeignKey(Book, null=True, blank=True, on_delete=models.CASCADE, related_name='files')
    total_views = models.IntegerField(null=True, default=0)
    storage_name = models.CharField(max_length=256, null=False, blank=False, default="empty", unique=True)
    episode = models.PositiveIntegerField(default=0, null=False, unique=True)
    
    def __str__(self):
        return self.title
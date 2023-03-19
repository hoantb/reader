from django.db import models
from files.models import File


class Page(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='image_files')
    file = models.ForeignKey(File, null=True, blank=True, on_delete=models.SET_NULL, related_name='pages')
    number = models.IntegerField(null=False, default=0)
    text = models.TextField(null=True, blank=True)
    audio = models.FileField(null=True, blank=True, upload_to='audio_files')
    
    def __str__(self):
        return self.file.title + ": page " + str(self.number)

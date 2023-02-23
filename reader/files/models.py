from django.db import models


class File(models.Model):
    title = models.TextField(null=False, blank=False)
    file = models.FileField(null=True, blank=True, upload_to='files')
    image_preview = models.ImageField(null=True, blank=True,upload_to='files')
    
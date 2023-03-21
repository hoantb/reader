from django.db import models
from files.models import File


class Page(models.Model):
    def upload_page(instance, file_name):
        return instance.file.book.storage_name + "/" + instance.file.storage_name + "/page_" + str(instance.number) + "/" + file_name

    image = models.ImageField(null=True, blank=True, upload_to=upload_page)
    file = models.ForeignKey(File, null=True, blank=True, on_delete=models.CASCADE , related_name='pages')
    number = models.IntegerField(null=False, default=0)
    text = models.TextField(null=True, blank=True)
    audio = models.FileField(null=True, blank=True, upload_to=upload_page)
    
    def __str__(self):
        return self.file.title + ": page " + str(self.number)

from django.db import models

class Visitor(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='content/avatars')

    def __str__(self):
        return self.name 
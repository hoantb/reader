from django.contrib import admin
from files.models import File

class FileAdmin(admin.ModelAdmin):
    pass

admin.site.register(File, FileAdmin)
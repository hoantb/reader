from django.contrib import admin
from visitors.models import Visitor

class VisitorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Visitor, VisitorAdmin)
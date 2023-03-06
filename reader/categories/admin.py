from django.contrib import admin
from categories.models import BookCategory

# Register your models here.
class BookCategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(BookCategory, BookCategoryAdmin)

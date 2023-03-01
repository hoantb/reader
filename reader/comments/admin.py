from django.contrib import admin

from comments.models import CommentBook, CommentFile

class CommentBookAdmin(admin.ModelAdmin):
    pass

class CommentFileAdmin(admin.ModelAdmin):
    pass

admin.site.register(CommentBook, CommentBookAdmin)
admin.site.register(CommentFile, CommentFileAdmin)


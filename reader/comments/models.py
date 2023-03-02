from django.db import models
from books.models import Book
from files.models import File
from visitors.models import Visitor

class CommentBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments', null=False, blank=False)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE, related_name='comments_book', null=False, blank=False)
    comment = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.comment

class CommentFile(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='comments', null=False, blank=False)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE, related_name='comments_file', null=False, blank=False)
    comment = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.comment
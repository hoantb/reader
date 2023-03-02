from rest_framework import serializers
from books.models import Book
from files.serializers import FileSerializer
from comments.serializers import CommentBookSerializer

class BookSerializer(serializers.ModelSerializer):
    image_preview = serializers.SerializerMethodField()
    files = FileSerializer(many=True)
    comments = CommentBookSerializer(many=True)
    

    class Meta:
        model = Book
        fields = ('id', 'title', 'image_preview','description', 'files', 'comments', 'total_views')
    
    def get_image_preview(self, book):
        if book.image_preview:
            return book.image_preview.url
        return None
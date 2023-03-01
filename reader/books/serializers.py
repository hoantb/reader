from rest_framework import serializers
from books.models import Book
from files.serializers import FileSerializer


class BookSerializer(serializers.ModelSerializer):
    image_preview = serializers.SerializerMethodField()
    files = FileSerializer(many=True)
    

    class Meta:
        model = Book
        fields = ('id', 'title', 'image_preview','description', 'files')
    
    def get_image_preview(self, book):
        if book.image_preview:
            return book.image_preview.url
        return None
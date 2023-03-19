from rest_framework import serializers
from files.models import File
from pages.serializers import PageSerializer
from comments.serializers import CommentFileSerializer


class FileSerializer(serializers.ModelSerializer):
    comments = CommentFileSerializer(many=True)
    pages = PageSerializer(many=True)

    class Meta:
        model = File
        fields = ['id', 'description', 'image_preview', 'file', 'comments', 'title', 'total_views', 'pages']

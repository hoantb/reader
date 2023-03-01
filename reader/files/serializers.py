from rest_framework import serializers
from files.models import File
from comments.serializers import CommentFileSerializer


class FileSerializer(serializers.ModelSerializer):
    comments = CommentFileSerializer(many=True)

    class Meta:
        model = File
        fields = ['id', 'description', 'image_preview', 'file', 'comments']
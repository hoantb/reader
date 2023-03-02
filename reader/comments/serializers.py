from rest_framework import serializers
from comments.models import CommentBook, CommentFile
from visitors.serializers import VisitorSerializer

class CommentBookSerializer(serializers.ModelSerializer):
    visitor = VisitorSerializer()

    class Meta:
        model = CommentBook
        fields = ['id', 'visitor', 'comment', 'date']

class CommentFileSerializer(serializers.ModelSerializer):
    visitor = VisitorSerializer()

    class Meta:
        model = CommentFile
        fields = ['id', 'visitor', 'comment', 'date']
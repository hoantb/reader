from rest_framework import serializers
from comments.models import CommentBook, CommentFile


class CommentBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentBook
        fields = '__all__'

class CommentFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentFile
        fields = '__all__'
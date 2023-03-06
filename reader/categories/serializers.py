from rest_framework import serializers
from categories.models import BookCategory

class BookCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = BookCategory
        fields = ('id', 'name')

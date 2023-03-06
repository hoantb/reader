from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from categories.models import BookCategory
from categories.serializers import BookCategorySerializer

class BookCategoryViewSet(viewsets.ViewSet):
    """
    viewset book categories
    """
    def list(self, request):
        queryset = BookCategory.objects.all()
        serializer = BookCategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = BookCategory.objects.all()
        category = get_object_or_404(queryset, pk=pk)
        serializer = BookCategorySerializer(category)
        return Response(serializer.data)

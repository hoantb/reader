from rest_framework import viewsets
from books.models import Book
from django.shortcuts import get_object_or_404
from books.serializers import BookSerializer
from rest_framework.response import Response


class BookiewSet(viewsets.ViewSet):
    """
    Book view set
    """
    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Book.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = BookSerializer(user)
        return Response(serializer.data)



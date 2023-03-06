from rest_framework import viewsets, mixins
from books.models import Book
from django.shortcuts import get_object_or_404
from books.serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import pagination
from django.core.paginator import Paginator

class ListModelViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    pass

class BookPagination(pagination.PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 50

class BookViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    Book view set
    """
    serializer_class = BookSerializer
    pagination_class = BookPagination

    def get_queryset(self):
        return Book.objects.all()

    def list(self, request):
        search_title = request.GET.get('title', None)
        filter_type = request.GET.get('sort-type', None)
        queryset = self.get_queryset()
        if filter_type == "latest":
            queryset = queryset.order_by('-date_created')
        elif filter_type == "popular":
            queryset = queryset.order_by('-total_views')
        elif filter_type == "rating":
            queryset = queryset
        else:
            queryset = queryset.order_by('title')
        if search_title and search_title.strip() != "":
            queryset = queryset.filter(title__contains=search_title)
        serializer = BookSerializer(queryset, many=True)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        book.total_views += 1
        book.save()
        serializer = BookSerializer(book)
        return Response(serializer.data)



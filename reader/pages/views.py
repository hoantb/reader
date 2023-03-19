from rest_framework import viewsets
from pages.models import Page
from django.shortcuts import get_object_or_404
from pages.serializers import PageSerializer
from rest_framework.response import Response


class PageViewSet(viewsets.ViewSet):
    """
    Page viewset
    """
    def list(self, request):
        queryset = Page.objects.all()
        serializer = PageSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Page.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = PageSerializer(user)
        return Response(serializer.data)



from rest_framework import viewsets
from files.models import File
from django.shortcuts import get_object_or_404
from files.serializers import FileSerializer
from rest_framework.response import Response


class FileViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = File.objects.all()
        serializer = FileSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = File.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = FileSerializer(user)
        return Response(serializer.data)



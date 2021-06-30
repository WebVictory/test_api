from terminology.models import Element, Directory
from rest_framework import viewsets
from rest_framework import permissions
from terminology.serializers import ElementSerializer, DirectorySerializer


class ElementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Element.objects.all().order_by('code')
    serializer_class = ElementSerializer
    permission_classes = [permissions.IsAuthenticated]

    filterset_fields = ['parent', 'parent__version',]


class DirectoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Directory.objects.all()
    serializer_class = DirectorySerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['date', 'version',  ]
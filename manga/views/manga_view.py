from rest_framework import viewsets
from manga.serializers.manga_serializer import MangaSerializer
from manga.models.manga import Manga

class MangaViewSet(viewsets.ModelViewSet):
    """
    View para manga
    """
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    search_fields = ['titulo']

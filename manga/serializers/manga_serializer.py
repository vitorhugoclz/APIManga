from rest_framework import serializers
from manga.models.manga import Manga

class MangaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = '__all__'
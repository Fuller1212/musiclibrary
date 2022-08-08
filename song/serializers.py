from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'album', 'release_date', 'genre', 'like']
        like = serializers.IntegerField(read_only= True)
from rest_framework import serializers
from .models import Song, User

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'genre', 'mood', 'popularity']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'listening_history', 'liked_songs', 'skipped_songs', 'preferred_genres', 'preferred_moods']
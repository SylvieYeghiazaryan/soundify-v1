from rest_framework import serializers
from .models import Song, User


class SongSerializer(serializers.ModelSerializer):
    """
    Serializer for the Song model.

    Serializes all relevant fields to represent a song instance,
    including its title, artist, genre, mood, and popularity.
    """

    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'genre', 'mood', 'popularity']


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.

    Serializes user profile data including preferences, liked/skipped songs, and listening history.
    Note: 'listening_history' must be a related name and would require a nested or custom serializer
    if you want to serialize full history details.
    """

    class Meta:
        model = User
        fields = ['id', 'name', 'listening_history', 'liked_songs', 'skipped_songs', 'preferred_genres',
                  'preferred_moods']

from django.db import models
from django.utils.timezone import now
from django.contrib.auth.hashers import make_password, check_password

GENRES = [
    "Pop", "Rock", "Jazz", "Hip-Hop", "Classical", "Electronic", "Reggae",
    "Country", "Blues", "R&B", "Metal", "Folk", "Soul"
]

MOODS = [
    "Happy", "Sad", "Energetic", "Relaxing", "Romantic", "Melancholic",
    "Angry", "Excited", "Chill"
]

TIME_OF_DAY = ["Morning", "Afternoon", "Evening"]

class Song(models.Model):
    """
    Represents a song in the music recommendation system.

    Attributes:
        title (str): Title of the song.
        artist (str): Name of the artist.
        genre (str): Genre of the song, selected from predefined choices.
        mood (str): Mood of the song, selected from predefined choices.
        popularity (int): Popularity score of the song (e.g., number of plays or likes).
    """
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    genre = models.CharField(max_length=100, choices=[(g, g) for g in GENRES])
    mood = models.CharField(max_length=100, choices=[(m, m) for m in MOODS])
    popularity = models.IntegerField(default=0)

    def __str__(self):
        """Return a string representation of the song."""
        return f"{self.title} - {self.artist}"


class User(models.Model):
    """
    Represents a user in the system.

    Attributes:
        name (str): Full name of the user.
        username (str): Unique username for the user.
        password (str): Hashed password (use set_password for security).
        liked_songs (QuerySet): Songs the user has liked.
        skipped_songs (QuerySet): Songs the user has skipped.
        preferred_genres (list): List of user's preferred genres.
        preferred_moods (list): List of user's preferred moods.
    """
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255, default="12345678")
    liked_songs = models.ManyToManyField("Song", related_name="liked_by", blank=True)
    skipped_songs = models.ManyToManyField("Song", related_name="skipped_by", blank=True)
    preferred_genres = models.JSONField(default=list)
    preferred_moods = models.JSONField(default=list)

    def set_password(self, raw_password):
        """
        Hash the provided raw password and save it securely.

        Args:
            raw_password (str): The raw password to be hashed and stored.
        """
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        """
        Verify that the given raw password matches the stored hashed password.

        Args:
            raw_password (str): The raw password to check.

        Returns:
            bool: True if the password matches, False otherwise.
        """
        return check_password(raw_password, self.password)

    def __str__(self):
        """Return the username as string representation of the user."""
        return self.username


class ListeningHistory(models.Model):
    """
    Records the listening history of users.

    Attributes:
        user (User): The user who listened to the song.
        song (Song): The song that was listened to.
        listened_at (datetime): The timestamp when the song was listened to.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listening_history")
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    listened_at = models.DateTimeField(default=now)

    def time_of_day(self):
        """
        Determine the time of day when the song was listened to.

        Returns:
            str: "Morning", "Afternoon", or "Evening" based on the hour.
        """
        hour = self.listened_at.hour
        if hour < 12:
            return "Morning"
        elif hour < 18:
            return "Afternoon"
        else:
            return "Evening"

    def __str__(self):
        """Return a human-readable record of the listening event."""
        return f"{self.user.name} - {self.song.title} at {self.listened_at}"


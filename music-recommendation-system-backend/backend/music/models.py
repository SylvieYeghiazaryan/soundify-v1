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
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    genre = models.CharField(max_length=100, choices=[(g, g) for g in GENRES])
    mood = models.CharField(max_length=100, choices=[(m, m) for m in MOODS])
    popularity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} - {self.artist}"

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=100, unique=True)  # Ensure uniqueness of username
    password = models.CharField(max_length=255, default="12345678")  # Use a default, but prefer setting it explicitly
    liked_songs = models.ManyToManyField("Song", related_name="liked_by", blank=True)
    skipped_songs = models.ManyToManyField("Song", related_name="skipped_by", blank=True)
    preferred_genres = models.JSONField(default=list)
    preferred_moods = models.JSONField(default=list)

    def set_password(self, raw_password):
        """Hash and save the password securely."""
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        """Check if the raw password matches the hashed password."""
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username

class ListeningHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listening_history")
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    listened_at = models.DateTimeField(default=now)

    def time_of_day(self):
        hour = self.listened_at.hour
        if hour < 12:
            return "Morning"
        elif hour < 18:
            return "Afternoon"
        else:
            return "Evening"

    def __str__(self):
        return f"{self.user.name} - {self.song.title} at {self.listened_at}"

import random
from django.core.management.base import BaseCommand
from music.models import Song, User, ListeningHistory
from datetime import datetime, timedelta
import pytz

# Define genres, moods
GENRES = ["Pop", "Rock", "Hip-Hop", "Jazz", "Classical", "Electronic", "Reggae", "Country"]
MOODS = ["Happy", "Sad", "Energetic", "Relaxing", "Romantic", "Melancholic"]

class Command(BaseCommand):
    help = "Generate synthetic data for users, songs, and listening history"

    def handle(self, *args, **kwargs):
        self.stdout.write("Generating synthetic data...")

        # Create songs
        songs = []
        for i in range(1000):
            song = Song.objects.create(
                title=f"Song {i}",
                artist=f"Artist {i % 20}",
                genre=random.choice(GENRES),
                mood=random.choice(MOODS),
                popularity=random.randint(1, 100)
            )
            songs.append(song)
        self.stdout.write("✅ Created 1000 songs.")

        # Create users
        users = []
        for i in range(100):
            user = User.objects.create(
                name=f"User {i}",
                username=f"user_{i}",
                preferred_genres=random.sample(GENRES, 3),
                preferred_moods=random.sample(MOODS, 2),
            )
            user.set_password("password123")
            users.append(user)
        self.stdout.write("✅ Created 100 users.")

        # Create listening history
        tz = pytz.UTC
        for user in users:
            for _ in range(random.randint(10, 30)):
                song = random.choice(songs)
                listened_at = tz.localize(datetime.now() - timedelta(days=random.randint(0, 30)))
                ListeningHistory.objects.create(user=user, song=song, listened_at=listened_at)
        self.stdout.write("✅ Created listening history for all users.")

        self.stdout.write(self.style.SUCCESS("🎵 Synthetic data generated successfully!"))
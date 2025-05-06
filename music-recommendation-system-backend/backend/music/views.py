import json
import os
from django.utils.timezone import now
from dotenv import load_dotenv
from openai import OpenAI
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, ListeningHistory

client = OpenAI()

load_dotenv()

client.api_key = os.getenv('OPENAI_API_KEY')

def get_time_of_day():
    current_hour = now().hour
    if current_hour < 12:
        return "Morning"
    elif current_hour < 18:
        return "Afternoon"
    return "Evening"

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = get_object_or_404(User, username=username)
        if user.check_password(password):
            return Response({"user_id": user.id}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

class RecommendationView(APIView):
    def get(self, request, user_id):
        """Fetches song recommendations based on listening history for the same time of day."""
        user = get_object_or_404(User, id=user_id)
        current_time_of_day = get_time_of_day()

        # Retrieve last 20 songs listened during this time of day
        history = ListeningHistory.objects.filter(user=user).order_by("-listened_at")[:20]
        songs = [h.song for h in history if h.time_of_day() == current_time_of_day]

        # If no history, ask LLM to generate general recommendations
        if not songs:
            prompt = f"This is a music recommender system. The user has no recent listening history at this time. " \
                     f"Please recommend 20 songs that are generally popular and diverse across different genres and moods in JSON format."
        else:
            prompt = f"This is a music recommender system. The user has listened to these songs in the {current_time_of_day}: " \
                     f"{', '.join([f'{s.title} by {s.artist}' for s in songs])}. " \
                     f"Recommend 20 similar songs in JSON format."

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": prompt}]
        )

        recommendations = response.choices[0].message.content
        start_index = recommendations.find("[")
        end_index = recommendations.rfind("]") + 1

        recommendations = recommendations[start_index:end_index]
        try:
            recommendations = json.loads(recommendations)
        except json.JSONDecodeError:
            return Response({"error": "Failed to parse recommendations as JSON"}, status=400)

        return Response({"recommended_songs": recommendations}, status=200)


class FilteredRecommendationView(APIView):
    def get(self, request, user_id):
        """Filters recommendations based on genre, mood, or both."""
        user = get_object_or_404(User, id=user_id)
        genre = request.query_params.get("genre")
        mood = request.query_params.get("mood")

        if not genre and not mood:
            return Response({"error": "At least one filter (genre or mood) is required."}, status=400)

        history = ListeningHistory.objects.filter(user=user)
        if genre:
            history = history.filter(song__genre=genre)
        if mood:
            history = history.filter(song__mood=mood)

        history = history.order_by("-listened_at")[:20]
        songs = [h.song for h in history]

        if not songs:
            prompt = f"This is a music recommender system. "
            if genre:
                prompt += f"The user prefers the genre {genre}. "
            if mood:
                prompt += f"The user enjoys songs with a {mood} mood. "
            prompt += "Recommend 20 songs that match these preferences in JSON format."
        else:
            song_list = ', '.join([f"{s.title} by {s.artist}" for s in songs])
            prompt = f"This is a music recommender system. "
            if genre:
                prompt += f"The user enjoys the genre {genre}. "
            if mood:
                prompt += f"The user likes songs with a {mood} mood. "
            prompt += f"Here are some recently listened songs: {song_list}. Recommend 20 similar songs in JSON format."

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": prompt}]
        )

        recommendations = response.choices[0].message.content
        start_index = recommendations.find("[")
        end_index = recommendations.rfind("]") + 1

        recommendations = recommendations[start_index:end_index]
        try:
            recommendations = json.loads(recommendations)
        except json.JSONDecodeError:
            return Response({"error": "Failed to parse recommendations as JSON"}, status=400)

        return Response({"recommended_songs": recommendations}, status=200)

class SearchRecommendationView(APIView):
    permission_classes = [AllowAny]
    parser_classes = [JSONParser]

    def post(self, request):
        """Allows user to search for songs using a natural language prompt."""
        query = request.data.get("query", "")

        if not query:
            return Response({"error": "Query is required."}, status=400)

        prompt = f"This is a music recommender system. The user asks: '{query}'. " \
                 f"Provide up to 20 relevant song recommendations in JSON format."

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": prompt}]
        )

        recommendations = response.choices[0].message.content
        start_index = recommendations.find("[")
        end_index = recommendations.rfind("]") + 1

        recommendations = recommendations[start_index:end_index]
        try:
            recommendations = json.loads(recommendations)
        except json.JSONDecodeError:
            return Response({"error": "Failed to parse recommendations as JSON"}, status=400)

        return Response({"recommended_songs": recommendations}, status=200)

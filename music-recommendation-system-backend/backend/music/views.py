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

# Load OpenAI API key
load_dotenv()
client = OpenAI()
client.api_key = os.getenv('OPENAI_API_KEY')


def get_time_of_day():
    """
    Determines the current time of day.

    Returns:
        str: One of "Morning", "Afternoon", or "Evening".
    """
    current_hour = now().hour
    if current_hour < 12:
        return "Morning"
    elif current_hour < 18:
        return "Afternoon"
    return "Evening"


class LoginView(APIView):
    """
    API endpoint for user login authentication.

    POST:
        - username: str
        - password: str

    Returns:
        - 200 OK with user_id if credentials are valid.
        - 400 Bad Request if invalid credentials.
    """

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = get_object_or_404(User, username=username)
        if user.check_password(password):
            return Response({"user_id": user.id}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


class RecommendationView(APIView):
    """
    API endpoint for recommending songs based on user's listening history
    at the current time of day (Morning, Afternoon, Evening).

    GET:
        - user_id: int

    Returns:
        - 200 OK with a list of recommended songs in JSON.
        - 400 if recommendation parsing fails.
    """

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        current_time_of_day = get_time_of_day()

        # Filter last 20 songs and retain only those from the current time of day
        history = ListeningHistory.objects.filter(user=user).order_by("-listened_at")[:20]
        songs = [h.song for h in history if h.time_of_day() == current_time_of_day]

        # Construct LLM prompt
        if not songs:
            prompt = (
                f"This is a music recommender system. The user has no recent listening history at this time. "
                f"Please recommend 20 songs that are generally popular and diverse across different genres and moods in JSON format."
            )
        else:
            song_list = ', '.join([f"{s.title} by {s.artist}" for s in songs])
            prompt = (
                f"This is a music recommender system. The user has listened to these songs in the {current_time_of_day}: "
                f"{song_list}. Recommend 20 similar songs in JSON format."
            )

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": prompt}]
        )

        recommendations = response.choices[0].message.content
        start_index = recommendations.find("[")
        end_index = recommendations.rfind("]") + 1

        try:
            recommendations = json.loads(recommendations[start_index:end_index])
        except json.JSONDecodeError:
            return Response({"error": "Failed to parse recommendations as JSON"}, status=400)

        return Response({"recommended_songs": recommendations}, status=200)


class FilteredRecommendationView(APIView):
    """
    API endpoint for song recommendations filtered by genre, mood, or both.

    GET:
        - user_id: int
        - genre: str (optional)
        - mood: str (optional)

    Returns:
        - 200 OK with filtered recommendations.
        - 400 if no filters or JSON parsing fails.
    """

    def get(self, request, user_id):
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

        # Construct prompt for LLM
        if not songs:
            prompt = "This is a music recommender system. "
            if genre:
                prompt += f"The user prefers the genre {genre}. "
            if mood:
                prompt += f"The user enjoys songs with a {mood} mood. "
            prompt += "Recommend 20 songs that match these preferences in JSON format."
        else:
            song_list = ', '.join([f"{s.title} by {s.artist}" for s in songs])
            prompt = "This is a music recommender system. "
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

        try:
            recommendations = json.loads(recommendations[start_index:end_index])
        except json.JSONDecodeError:
            return Response({"error": "Failed to parse recommendations as JSON"}, status=400)

        return Response({"recommended_songs": recommendations}, status=200)


class SearchRecommendationView(APIView):
    """
    API endpoint for generating recommendations using a natural language query.

    POST:
        - query: str (e.g., "Relaxing music for evening walks")

    Returns:
        - 200 OK with song recommendations based on query.
        - 400 if query is missing or parsing fails.
    """
    permission_classes = [AllowAny]
    parser_classes = [JSONParser]

    def post(self, request):
        query = request.data.get("query", "")

        if not query:
            return Response({"error": "Query is required."}, status=400)

        prompt = (
            f"This is a music recommender system. The user asks: '{query}'. "
            f"Provide up to 20 relevant song recommendations in JSON format."
        )

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": prompt}]
        )

        recommendations = response.choices[0].message.content
        start_index = recommendations.find("[")
        end_index = recommendations.rfind("]") + 1

        try:
            recommendations = json.loads(recommendations[start_index:end_index])
        except json.JSONDecodeError:
            return Response({"error": "Failed to parse recommendations as JSON"}, status=400)

        return Response({"recommended_songs": recommendations}, status=200)
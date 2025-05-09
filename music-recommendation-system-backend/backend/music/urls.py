from django.urls import path
from .views import (
    RecommendationView,
    SearchRecommendationView,
    FilteredRecommendationView,
    LoginView
)

# URL patterns for the music recommendation API
urlpatterns = [
    # User login endpoint
    path("login/", LoginView.as_view(), name="login"),

    # Get personalized recommendations based on time of day and listening history
    path("recommendations/<int:user_id>/", RecommendationView.as_view(), name="recommendations"),

    # Get filtered recommendations based on genre/mood
    path("recommendations/filter/<int:user_id>/", FilteredRecommendationView.as_view(),
         name="filtered-recommendations"),

    # Natural language search-based recommendations
    path("recommendations/search/", SearchRecommendationView.as_view(), name="search-recommendations"),
]


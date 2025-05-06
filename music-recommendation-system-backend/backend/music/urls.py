from django.urls import path
from .views import (
    RecommendationView,
    SearchRecommendationView, FilteredRecommendationView, LoginView
)

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("recommendations/<int:user_id>/", RecommendationView.as_view(), name="recommendations"),
    path("recommendations/filter/<int:user_id>/", FilteredRecommendationView.as_view(), name="filtered-recommendations"),
    path("recommendations/search/", SearchRecommendationView.as_view(), name="search-recommendations"),
]

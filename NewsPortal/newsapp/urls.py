from django.urls import path
from .views import NEWS, NEWSOne


urlpatterns = [
    path('', NEWS.as_view()),
    path('<int:pk>', NEWSOne.as_view()),
]
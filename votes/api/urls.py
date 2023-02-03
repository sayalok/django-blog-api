from django.urls import path
from .views import VoteCreate

urlpatterns = [
    path('', VoteCreate.as_view()),
]
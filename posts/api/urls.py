from django.urls import path
from .views import PostList, PostRetriveUpdateDestroy

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostRetriveUpdateDestroy.as_view()),
]
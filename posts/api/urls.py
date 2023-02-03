from django.urls import path
from .views import PostList,PostRetriveDestroy

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostRetriveDestroy.as_view()),
]
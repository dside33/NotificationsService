from django.urls import path
from .views import CustomUserListAPIView


urlpatterns = [
    path('api/', CustomUserListAPIView.as_view(), name='users_list'),
]

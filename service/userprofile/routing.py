from django.urls import path

from .consumers import ProfileConsumer


ws_urlpatterns = [
    path('ws/profile/', ProfileConsumer.as_asgi()),
]
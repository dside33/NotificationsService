from django.urls import path
from .views import JSONSendAPIView, CSVSendAPIView, MainPageView


urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
    path('api/json/', JSONSendAPIView.as_view()),
    path('api/csv/', CSVSendAPIView.as_view()),
]

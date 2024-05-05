from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import CustomUser
from .serializers import CustomUserSerializer

from .utils import send_email
import json


class CustomUserListAPIView(APIView):
    
    def post(self, request, format=None):
        # custom_users = CustomUser.objects.all()
        # serializer = CustomUserSerializer(custom_users, many=True)

        # users = serializer.data
        
        users_data = request.data.get('users')
        
        if not users_data:
            return Response({"error": "No users provided in JSON data."}, status=400)
        
        for user in users_data:
            method = user.get('notification_method', '')
                
            if method == CustomUser.EMAIL:    
                send_email.delay(user.get('notification_address'))
        
        return Response({"status": "Success"}, status=200)



from rest_framework import serializers
from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'notification_method', 'notification_address'] 

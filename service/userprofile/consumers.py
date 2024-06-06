from channels.generic.websocket import WebsocketConsumer
from django.core.cache import cache

from django.utils.crypto import get_random_string
import json

from userprofile.models import APIKey


class ProfileConsumer(WebsocketConsumer):
    def connect(self):
        user = self.scope['user']
        if user.is_anonymous:
            self.close()
        else:
            self.accept()
            self.send(text_data=json.dumps({
                'message': f'Hello, {user.username}'
            }))

        self.send(text_data=json.dumps({'message': 'yo'}))
        self.send_api_keys()
    
    def disconnect(self, close_code):
        print(f"Disconnected with close code: {close_code}")

    def receive(self, text_data):
        data = json.loads(text_data)
        message_type = data.get('type', '')

        self.send(text_data=json.dumps({'message': message_type}))
        
        if message_type == 'delete_api_key':
            self.delete_api_key(data['value'])
        elif message_type == 'create_api_key':
            self.create_api_key()

    def send_api_keys(self):
        user = self.scope['user']
        cache_key = f"api_keys_{user.id}"
        api_keys = cache.get(cache_key)

        if not api_keys:
            api_keys = APIKey.objects.filter(user=user)
            cache.set(cache_key, api_keys, timeout=60*60)

        self.send(text_data=json.dumps({
            'type': 'api_keys',
            'api_keys': [{'value': key.value} for key in api_keys]
        }))

    def delete_api_key(self, value):
        user = self.scope['user']
        cache_key = f"api_keys_{user.id}"

        APIKey.objects.filter(user=user, value=value).delete()

        api_keys = APIKey.objects.filter(user=user)
        cache.set(cache_key, api_keys, timeout=60*60)

        self.send(text_data=json.dumps({'message': 'deleted'}))

        self.send(text_data=json.dumps({
            'type': 'api_keys',
            'api_keys': [{'value': key.value} for key in api_keys]
        }))

    def create_api_key(self):
        user = self.scope['user']
        cache_key = f"api_keys_{user.id}"

        APIKey.objects.create(user=user, value=get_random_string(length=32))

        api_keys = APIKey.objects.filter(user=user)

        cache.set(cache_key, api_keys, timeout=60*60)

        self.send(text_data=json.dumps({
            'type': 'api_keys',
            'api_keys': [{'value': key.value} for key in api_keys]
        }))



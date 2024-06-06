from django.db.models.signals import post_save  
from django.dispatch import receiver
from django.core.cache import cache
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .models import APIKey


@receiver(post_save, sender=APIKey)
def update_api_keys(sender, instance, **kwargs):
    user = instance.user
    api_keys = list(APIKey.objects.filter(user=user).values('value', 'created_at'))

    cache_key = f'api_keys_{user.id}'
    cache.set(cache_key, api_keys, timeout=60*60)
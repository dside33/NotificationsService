from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    TELEGRAM = 'Telegram'
    SMS = 'SMS'
    EMAIL = 'Email'

    NOTIFICATION_CHOICES = [
        (TELEGRAM, 'Telegram'),
        (SMS, 'SMS'),
        (EMAIL, 'Email'),
    ]

    notification_method = models.CharField(
                                            max_length=10,
                                            choices=NOTIFICATION_CHOICES,
                                            default='Email',
                                            verbose_name='Способ оповещения'
                                        )
    
    notification_address = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.username

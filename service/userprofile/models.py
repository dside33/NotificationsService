from django.db import models

from users.models import CustomUser


def user_directory_path(instance, filename):
    return f'user_{instance.user.id}/{filename}'


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, null=True, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, upload_to=user_directory_path)

    def __str__(self):
        return f'Профиль - {str(self.user.username)}'



class APIKey(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    value = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.value

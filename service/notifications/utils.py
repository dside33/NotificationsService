from django.core.mail import send_mail
from celery import shared_task

from users.models import CustomUser

import json


@shared_task
def send_email(user_email):
    send_mail(
        "Не может быть, это работает!",
        "Это письмо чтобы убедиться, что это работает.",
        "not1ficationservice599@gmail.com",
        [user_email],
        fail_silently=False,
    )


def check_json_file(file_obj):
    if not file_obj:
        return False, "No file provided."

    try:
        with file_obj:
            users = json.load(file_obj)
    except Exception as e:
        return False, f"Error with reading file: {e}"

    if not users:
        return False, "No users found in JSON file."
    
    for user in users:
        if user.get('notification_method') == CustomUser.EMAIL:
            send_email.delay(user.get('notification_address'))

    return True, "Success"

from django.core.mail import send_mail
from celery import shared_task


@shared_task
def send_email(user_email):
    send_mail(
        "Не может быть, это работает!",
        "Это письмо чтобы убедиться, что это работает.",
        "not1ficationservice599@gmail.com",
        [user_email],
        fail_silently=False,
    )




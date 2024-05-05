from django.db import models


class EmergencyMail(models.Model):
    text_mail = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Emergency Email ({self.created_at})"

    def format_text(self, username):
        return self.text_mail.format(username=username)

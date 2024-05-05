# Generated by Django 3.2.16 on 2024-05-01 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='notification_address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='customuser',
            name='notification_method',
            field=models.CharField(choices=[('Telegram', 'Telegram'), ('SMS', 'SMS'), ('Email', 'Email')], default='Email', max_length=10, verbose_name='Способ оповещения'),
        ),
    ]

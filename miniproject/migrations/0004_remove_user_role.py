# Generated by Django 5.0.7 on 2024-07-14 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniproject', '0003_delete_event_user_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]

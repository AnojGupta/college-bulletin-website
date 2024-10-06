# Generated by Django 5.0.7 on 2024-07-14 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniproject', '0002_user_placement_news'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('moderator', 'Moderator'), ('user', 'User')], default='user', max_length=20),
        ),
    ]

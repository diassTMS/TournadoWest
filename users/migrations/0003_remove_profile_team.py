# Generated by Django 5.0.7 on 2024-07-16 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='team',
        ),
    ]
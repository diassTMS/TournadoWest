# Generated by Django 5.0.7 on 2024-07-25 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0002_remove_league_breakduration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leaguematch',
            old_name='tournament',
            new_name='league',
        ),
    ]
# Generated by Django 5.0.7 on 2024-07-14 09:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('age', models.CharField(choices=[('U8', 'Under 8s'), ('U9', 'Under 9s'), ('U10', 'Under 10s'), ('U11', 'Under 11s'), ('U12', 'Under 12s'), ('U13', 'Under 13s'), ('U14', 'Under 14s'), ('U15', 'Under 15s'), ('U16', 'Under 16s'), ('U17', 'Under 17s'), ('U18', 'Under 18s'), ('Mixed', 'Mixed ages')], max_length=5)),
                ('gender', models.CharField(choices=[('Girls', 'Girls'), ('Boys', 'Boys'), ('Mixed', 'Mixed')], max_length=5)),
                ('date', models.DateTimeField()),
                ('venue', models.CharField(max_length=50)),
                ('noPitches', models.IntegerField()),
                ('noDivisions', models.IntegerField()),
                ('noTeams', models.IntegerField(default=0)),
                ('startTime', models.TimeField()),
                ('matchDuration', models.IntegerField(default=15)),
                ('halftimeDuration', models.IntegerField(default=0)),
                ('breakDuration', models.IntegerField(default=5)),
                ('knockoutRounds', models.CharField(choices=[('Final', 'Final'), ('Semis & Final', 'Semis & Final'), ('Playoffs, Semis & Final', 'Playoffs, Semis & Final'), ('None', 'None')], default='None', max_length=25)),
                ('liveScores', models.BooleanField(default=True)),
                ('generatedSchedule', models.BooleanField(default=False)),
                ('finished', models.BooleanField(default=False)),
                ('level', models.CharField(choices=[('Tier 1', 'Tier 1'), ('Tier 2', 'Tier 2'), ('Tier 3', 'Tier 3'), ('County', 'County'), ('Regional', 'Regional'), ('National', 'National'), ('N/A', 'N/A')], max_length=10)),
                ('group', models.CharField(choices=[('School', 'School'), ('Club', 'Club'), ('Social', 'Social'), ('County', 'County'), ('N/A', 'N/A')], max_length=7)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

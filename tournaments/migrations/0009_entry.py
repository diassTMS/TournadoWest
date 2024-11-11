# Generated by Django 5.0.7 on 2024-07-16 12:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0008_alter_tournament_livescores'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.IntegerField(default=0)),
                ('rank', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('won', models.IntegerField(default=0)),
                ('drawn', models.IntegerField(default=0)),
                ('lost', models.IntegerField(default=0)),
                ('forGoals', models.IntegerField(default=0)),
                ('againstGoals', models.IntegerField(default=0)),
                ('goalDiff', models.IntegerField(default=0)),
                ('played', models.IntegerField(default=0)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.tournament')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# Generated by Django 5.0.7 on 2024-09-22 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0012_remove_schedule_generated_remove_schedule_publishpdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
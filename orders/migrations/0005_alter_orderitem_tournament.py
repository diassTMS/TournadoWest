# Generated by Django 5.0.7 on 2024-10-31 22:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_rename_is_paid_order_paid'),
        ('tournaments', '0029_tournament_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.tournament'),
        ),
    ]

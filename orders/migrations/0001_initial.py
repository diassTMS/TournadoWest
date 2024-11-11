# Generated by Django 5.0.7 on 2024-08-02 22:04

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tournaments', '0024_remove_tournament_entryprice_currency_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('title', models.CharField(blank=True, max_length=150)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('value', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('final_value', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('is_paid', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('discount_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('final_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('total_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='orders.order')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tournaments.tournament')),
            ],
        ),
    ]

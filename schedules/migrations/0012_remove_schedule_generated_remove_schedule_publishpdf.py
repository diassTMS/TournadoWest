# Generated by Django 5.0.7 on 2024-07-21 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0011_rename_pdf_schedule_publishpdf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='generated',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='publishPdf',
        ),
    ]
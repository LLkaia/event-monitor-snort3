# Generated by Django 4.2.7 on 2024-01-09 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shell', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiler',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

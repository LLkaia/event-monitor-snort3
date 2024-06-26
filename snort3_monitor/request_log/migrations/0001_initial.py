# Generated by Django 4.2.7 on 2023-12-18 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_addr', models.CharField(max_length=50)),
                ('http_method', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('endpoint', models.CharField(max_length=128)),
                ('response', models.IntegerField()),
                ('request_data', models.JSONField()),
            ],
        ),
    ]

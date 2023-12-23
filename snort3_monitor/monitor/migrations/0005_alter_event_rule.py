# Generated by Django 4.2.7 on 2023-12-22 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rule', '0002_rule_deprecated'),
        ('monitor', '0004_delete_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='rule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rule.rule'),
        ),
    ]

# Generated by Django 3.2.21 on 2023-10-19 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0009_auto_20231019_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='completed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]

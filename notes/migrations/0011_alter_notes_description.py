# Generated by Django 3.2.21 on 2023-10-24 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0010_alter_notes_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='description',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]

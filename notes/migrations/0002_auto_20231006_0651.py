# Generated by Django 3.2.21 on 2023-10-06 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='description',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='notes',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notes',
            name='title',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
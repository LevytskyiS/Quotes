# Generated by Django 5.0 on 2023-12-20 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]

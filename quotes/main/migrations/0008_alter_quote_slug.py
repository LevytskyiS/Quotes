# Generated by Django 5.0 on 2023-12-21 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_quote_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='slug',
            field=models.SlugField(default='1703157365.835789', max_length=255),
        ),
    ]

# Generated by Django 2.2.28 on 2025-03-14 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stroll', '0004_auto_20250314_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='walk',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]

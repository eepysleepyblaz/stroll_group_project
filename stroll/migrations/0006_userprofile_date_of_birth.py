# Generated by Django 2.2.28 on 2025-03-22 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stroll', '0005_remove_userprofile_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]

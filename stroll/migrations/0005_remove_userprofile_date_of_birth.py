# Generated by Django 2.2.28 on 2025-03-22 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stroll', '0004_userprofile_date_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='date_of_birth',
        ),
    ]

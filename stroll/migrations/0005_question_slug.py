# Generated by Django 2.2.28 on 2025-03-23 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stroll', '0004_question_comment_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='slug',
            field=models.CharField(default='a', max_length=1),
        ),
    ]

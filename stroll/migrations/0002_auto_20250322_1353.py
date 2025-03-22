# Generated by Django 2.2.28 on 2025-03-22 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stroll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questioncomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stroll.UserProfile'),
        ),
        migrations.AlterField(
            model_name='walkcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stroll.UserProfile'),
        ),
    ]

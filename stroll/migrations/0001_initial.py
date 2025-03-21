# Generated by Django 2.2.28 on 2025-03-22 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_published', models.DateField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=300)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='Walk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('area', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('date_published', models.DateField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('difficulty', models.IntegerField(default=0)),
                ('length', models.IntegerField(default=0)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='walk_photos/')),
                ('tags', models.CharField(blank=True, max_length=255, null=True)),
                ('gallery_image_1', models.ImageField(blank=True, null=True, upload_to='walk_photos/')),
                ('gallery_image_2', models.ImageField(blank=True, null=True, upload_to='walk_photos/')),
                ('gallery_image_3', models.ImageField(blank=True, null=True, upload_to='walk_photos/')),
                ('gallery_image_4', models.ImageField(blank=True, null=True, upload_to='walk_photos/')),
                ('map_coordinates', models.CharField(max_length=5000, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Walks',
            },
        ),
        migrations.CreateModel(
            name='WalkComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_published', models.DateField(auto_now_add=True)),
                ('text', models.CharField(max_length=300)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('walk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stroll.Walk')),
            ],
            options={
                'verbose_name_plural': 'Walk Comments',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_moderator', models.BooleanField(blank=True, default=False)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('total_likes', models.IntegerField(default=0)),
                ('total_views', models.IntegerField(default=0)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='QuestionComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_published', models.DateField(auto_now_add=True)),
                ('text', models.CharField(max_length=300)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stroll.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Question Comments',
            },
        ),
    ]

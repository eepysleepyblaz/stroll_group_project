# Generated by Django 2.2.28 on 2025-03-10 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_published', models.DateField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('description', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=12)),
                ('is_moderator', models.BooleanField()),
                ('total_likes', models.IntegerField(default=0)),
                ('total_views', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Walk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('area', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=1000)),
                ('date_published', models.DateField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('difficulty', models.IntegerField(default=0)),
                ('length', models.IntegerField(default=0)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='walks/')),
                ('tags', models.CharField(max_length=255)),
                ('gallery_image_1', models.ImageField(blank=True, null=True, upload_to='gallery/')),
                ('gallery_image_2', models.ImageField(blank=True, null=True, upload_to='gallery/')),
                ('gallery_image_3', models.ImageField(blank=True, null=True, upload_to='gallery/')),
                ('gallery_image_4', models.ImageField(blank=True, null=True, upload_to='gallery/')),
                ('map_coordinates', models.CharField(max_length=5000, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stroll.User')),
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
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stroll.User')),
                ('walk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stroll.Walk')),
            ],
            options={
                'verbose_name_plural': 'Walk Comments',
            },
        ),
        migrations.CreateModel(
            name='QuestionComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_published', models.DateField(auto_now_add=True)),
                ('text', models.CharField(max_length=300)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stroll.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stroll.User')),
            ],
            options={
                'verbose_name_plural': 'Question Comments',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stroll.User'),
        ),
    ]

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    description = models.CharField(max_length=500)
    password = models.CharField(max_length=12)
    is_moderator = models.BooleanField()
    total_likes = models.IntegerField(default=0)
    total_views = models.IntegerField(default=0)

class Walk(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Foreign key
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    date_published = models.DateField.auto_now_add
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=0)
    length = models.IntegerField(default=0)
    thumbnail = models.ImageField(upload_to='walks/')
    tags = models.CharField(max_length=255)
    gallery_image_1 = models.ImageField(upload_to='gallery/')
    gallery_image_2 = models.ImageField(upload_to='gallery/')
    gallery_image_3 = models.ImageField(upload_to='gallery/')
    gallery_image_4 = models.ImageField(upload_to='gallery/')
    map_coordinates = models.CharField(max_length=5000)


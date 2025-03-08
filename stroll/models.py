from django.db import models

class User(models.Model):
    username = models.CharField(max_length = 30)
    date_of_birth = models.DateField()
    description = models.CharField(max_length = 500)
    password = models.CharField(max_length = 12)
    is_moderator = models.BooleanField()
    total_likes = models.IntegerField()
    total_views = models.IntegerField()

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    is_moderator = models.BooleanField(default=False, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    total_likes = models.IntegerField(default=0)
    total_views = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.user.username



class Walk(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Foreign key
    title = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    description = models.CharField(max_length=1000, null=True, blank=True)
    date_published = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=0)
    length = models.IntegerField(default=0)
    thumbnail = models.ImageField(upload_to='walk_photos/', null=True, blank=True)
    tags = models.CharField(max_length=255, null=True, blank=True)
    gallery_image_1 = models.ImageField(upload_to='walk_photos/', null=True, blank=True)
    gallery_image_2 = models.ImageField(upload_to='walk_photos/', null=True, blank=True)
    gallery_image_3 = models.ImageField(upload_to='walk_photos/', null=True, blank=True)
    gallery_image_4 = models.ImageField(upload_to='walk_photos/', null=True, blank=True)
    map_coordinates = models.CharField(max_length=5000, null=True)

    class Meta:
        verbose_name_plural = 'Walks'

    def __str__(self):
        return self.title, self.area
    


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Foreign key
    date_published = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=300)
    class Meta:
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.title



class WalkComment(models.Model):
    walk = models.ForeignKey(Walk, on_delete=models.CASCADE) # Foreign key
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Foreign key
    date_published = models.DateField(auto_now_add=True)
    text = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = 'Walk Comments'

    def __str__(self):
        return self.text



class QuestionComment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # Foreign key
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Foreign key
    date_published = models.DateField(auto_now_add=True)
    text = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = 'Question Comments'

    def __str__(self):
        return self.text
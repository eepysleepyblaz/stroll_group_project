from django.db import models
from django.contrib.auth.models import User
import os

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    is_moderator = models.BooleanField(default=False, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    total_likes = models.IntegerField(default=0)
    total_views = models.IntegerField(default=0)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'UserProfiles'
    
    def delete(self,*args,**kwargs):
        for image in [self.profile_picture]:
            try:
                if os.path.isfile(image.path):
                    os.remove(image.path)
            except ValueError:
                pass

        super(UserProfile, self).delete(*args,**kwargs)

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
    thumbnail = models.ImageField(upload_to='walk_thumbnails/', null=True, blank=True)
    tags = models.CharField(max_length=255, null=True, blank=True)
    gallery_image_1 = models.ImageField(upload_to='walk_gelleries/', null=True, blank=True)
    gallery_image_2 = models.ImageField(upload_to='walk_galleries/', null=True, blank=True)
    gallery_image_3 = models.ImageField(upload_to='walk_galleries/', null=True, blank=True)
    gallery_image_4 = models.ImageField(upload_to='walk_galleries/', null=True, blank=True)
    map_coordinates = models.CharField(max_length=5000, null=True)

    class Meta:
        verbose_name_plural = 'Walks'
    
    def delete(self,*args,**kwargs):
        for image in [self.thumbnail, self.gallery_image_1, self.gallery_image_2, self.gallery_image_3, self.gallery_image_4]:
            try:
                if os.path.isfile(image.path):
                    os.remove(image.path)
            except ValueError:
                pass

        super(Walk, self).delete(*args,**kwargs)
    
    def tags_as_list(self):
        return self.tags.split(",")

    def __str__(self):
        return f"{self.title} {self.area}"
    


class Question(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE) # Foreign key
    date_published = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    question = models.CharField(max_length=100)
    comment_count = models.IntegerField(default=0)
    slug = models.CharField(max_length=1, default='a')
    class Meta:
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.question



class WalkComment(models.Model):
    walk = models.ForeignKey(Walk, on_delete=models.CASCADE) # Foreign key
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE) # Foreign key
    date_published = models.DateField(auto_now_add=True)
    comment = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = 'Walk Comments'

    def __str__(self):
        return self.comment



class QuestionComment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # Foreign key
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE) # Foreign key
    date_published = models.DateField(auto_now_add=True)
    comment = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = 'Question Comments'

    def __str__(self):
        return self.comment
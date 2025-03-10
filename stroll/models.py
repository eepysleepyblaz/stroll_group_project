from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=500)
    password = models.CharField(max_length=12)
    is_moderator = models.BooleanField(default=False)
    total_likes = models.IntegerField(default=0)
    total_views = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username



class Walk(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Foreign key
    title = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    date_published = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=0)
    length = models.IntegerField(default=0)
    thumbnail = models.ImageField(upload_to='walks/', null=True, blank=True)
    tags = models.CharField(max_length=255)
    gallery_image_1 = models.ImageField(upload_to='gallery/', null=True, blank=True)
    gallery_image_2 = models.ImageField(upload_to='gallery/', null=True, blank=True)
    gallery_image_3 = models.ImageField(upload_to='gallery/', null=True, blank=True)
    gallery_image_4 = models.ImageField(upload_to='gallery/', null=True, blank=True)
    map_coordinates = models.CharField(max_length=5000, null=True)

    class Meta:
        verbose_name_plural = 'Walks'

    def __str__(self):
        return self.title
    


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Foreign key
    date_published = models.DateField(auto_now_add=True)
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
from django import forms
from django.contrib.auth.models import User
from stroll.models import UserProfile, Walk

class CreateWalkForm(forms.ModelForm):
    title = forms.CharField(max_length=30, help_text="Title:")
    area = forms.CharField(max_length=30, help_text="Area:")
    description = forms.CharField(max_length=1000, help_text="Description:")
    length = forms.IntegerField(min_value=0)
    difficulty = forms.IntegerField(min_value=0, max_value=10, help_text="Difficulty:")
    tags = forms.CharField(max_length=255, help_text="Tags:")
    thumbnail = forms.ImageField(widget=forms.ClearableFileInput(), help_text="Thumbnail", required=False)
    gallery_image_1 = forms.ImageField(widget=forms.ClearableFileInput(), help_text="Photo:", required=False)
    gallery_image_2 = forms.ImageField(widget=forms.ClearableFileInput(), help_text="Photo:", required=False)
    gallery_image_3 = forms.ImageField(widget=forms.ClearableFileInput(), help_text="Photo:", required=False)
    gallery_image_4 = forms.ImageField(widget=forms.ClearableFileInput(), help_text="Photo:", required=False)
    map_coordinates = forms.CharField(max_length=5000)

    class Meta:
        model = Walk
        fields = ('title', 'area', 'description', 'length','difficulty','tags','thumbnail','gallery_image_1','gallery_image_2','gallery_image_3','gallery_image_4','map_coordinates')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    date_of_birth = forms.DateField(widget=forms.DateInput(), required=False)
    email = forms.EmailField(widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_picture', 'description', 'date_of_birth')
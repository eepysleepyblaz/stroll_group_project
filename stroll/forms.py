from django import forms
from django.contrib.auth.models import User

from stroll.models import Walk

class CreateWalkForm(forms.ModelForm):
    title = forms.CharField(max_length=30, help_text="Title:")
    area = forms.CharField(max_length=30, help_text="Area:")
    description = forms.CharField(max_length=1000, help_text="Description:")
    length = forms.IntegerField(min_value=0, help_text="Length:")
    difficulty = forms.IntegerField(min_value=0, max_value=10, help_text="Difficulty:")
    tags = forms.CharField(max_length=255, help_text="Tags:")
    thumbnail = forms.ImageField(widget=forms.ClearableFileInput(), help_text="Thumbnail")
    photo = forms.ImageField(widget=forms.ClearableFileInput(), help_text="Photo:")
    map_coordinates = forms.CharField(max_length=5000)

    class Meta:
        model = Walk
        fields = ('title', 'area', 'description', 'length','difficulty','tags','thumbnail','photo')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    date_of_birth = forms.DateField(widget=forms.DateInput())
    picture = forms.ImageField(widget=forms.ClearableFileInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password','picture','date_of_birth')
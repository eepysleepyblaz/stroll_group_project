'''
Code based on chapter 18 Automated Testing from Tango with Django 2 
course textbook

Tests might take 20-30 seconds to complete.
'''

from django.test import TestCase
from django.urls import reverse
from stroll.models import Walk, UserProfile, Question, QuestionComment, WalkComment
from django.contrib.auth.models import User

class TestUserProfileModelDeletion(TestCase):
    def setUp(self):
        self.user = User(username='Test user', email='Test email')
        self.user.set_password('123')
        self.user.save()
        self.user_profile = UserProfile(user=self.user)
        self.user_profile.save()

        self.client.force_login(self.user)

    def test_user_profile_model_deletion(self):
        # Tests if the delete() function for UserProfile works, this test improves coverage greatly
        self.user_profile.delete()
        self.assertFalse(UserProfile.objects.filter(id=self.user_profile.id).exists())
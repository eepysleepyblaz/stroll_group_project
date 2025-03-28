'''
Code based on chapter 18 Automated Testing from Tango with Django 2 
course textbook

Tests might take 20-30 seconds to complete.
'''
from django.test import TestCase
from django.urls import reverse
from stroll.models import Walk, UserProfile, Question, QuestionComment, WalkComment
from django.contrib.auth.models import User

class TestUserProfileModels(TestCase):
    print('Standard tests for model deletion are running, this may take upto 10 seconds...')
    def setUp(self):
        self.user = User(username='Test user', email='Test email')
        self.user.set_password('123')
        self.user.save()
        self.user_profile = UserProfile(user=self.user)
        self.user_profile.save()

        self.walk = Walk(title='Test walk', user=self.user, tags='test,tags', thumbnail='population_thumbnails/test.jpg')
        self.walk.save()

        self.question = Question(user=self.user_profile)
        self.question.save()

        self.user_profile.refresh_from_db()

        self.client.force_login(self.user)

    def test_user_profile_model_deletion(self):
        # Tests if the delete() function for UserProfile works, this test improves test coverage greatly for models.py
        self.user_profile.delete()
        self.assertFalse(UserProfile.objects.filter(id=self.user_profile.id).exists())

    def tests_models_likes_and_views(self):
        self.assertTrue(self.walk.likes >= 0)
        self.assertTrue(self.walk.views >= 0)
        self.assertTrue(self.question.likes >= 0)
        self.assertTrue(self.question.views >= 0)
        self.assertTrue(self.user_profile.total_likes >= 0)
        self.assertTrue(self.user_profile.total_views >= 0)

    
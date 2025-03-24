from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from stroll.models import Walk, Question, WalkComment, UserProfile

class StrollTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.profile = UserProfile.objects.create(user=self.user)
        self.client.login(username='testuser', password='testpass')

    def test_login_redirects(self):
        self.client.logout()
        response = self.client.post(reverse('stroll:login'), {
            'username': 'testuser',
            'password': 'testpass'
        })
        self.assertEqual(response.status_code, 302)

    def test_create_walk_view(self):
        response = self.client.get(reverse('stroll:create_walk'))
        self.assertEqual(response.status_code, 200)

    def test_question_post(self):
        response = self.client.post(reverse('stroll:questions'), {
            'question': 'Is there a good sunset view?'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Question.objects.filter(question__icontains='sunset').exists())

    def test_walk_creation_and_comment(self):
        walk = Walk.objects.create(
            title="Sample Walk",
            area="Test Area",
            description="Test description",
            length=1000,
            difficulty=3,
            tags="test",
            user=self.user,
            thumbnail="test.jpg",
            map_coordinates="123,456"
        )

        response = self.client.post(reverse('stroll:show_walk', args=[walk.id]), {
            'comment': 'Nice walk!'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(WalkComment.objects.filter(walk=walk, comment='Nice walk!').exists())

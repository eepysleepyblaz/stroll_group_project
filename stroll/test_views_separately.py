from django.test import TestCase
from django.urls import reverse
from stroll.models import Walk, UserProfile, Question
from django.contrib.auth.models import User

class TestViewsProvideResponse(TestCase):
    def setUp(self):
        self.user = User(username='Test user', email='Test email')
        self.user.set_password('123')
        self.user.save()
        self.user_profile = UserProfile(user=self.user)
        self.user_profile.save()

        self.client.force_login(self.user)


        self.walk = Walk(title='Test walk', user=self.user, tags='test,tags', thumbnail='population_thumbnails/govan.jpg')
        self.walk.save()

        self.question = Question(user=self.user_profile)
        self.question.save()

    @classmethod
    def views_work_helper_except_show_walk_and_show_question(client, self, view_name):
        response = self.client.get(reverse(f'stroll:{view_name}'))
        if view_name == 'logout':
            self.assertRedirects(response, reverse('stroll:home'))
        else:
            self.assertEqual(response.status_code, 200)

    @classmethod
    def views_work_helper_except_show_walk_and_show_question_logged_out(client, self, view_name):
        self.client.logout()
        response = self.client.get(reverse(f'stroll:{view_name}'))
        if view_name == 'logout' or view_name == 'create_walk' or view_name == 'my_profile':
            if '_' in view_name:
                view_name = view_name.replace('_', '-')
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(response, f'/stroll/login/?next=/stroll/{view_name}/')
        elif view_name == 'my_walks' or view_name == 'my_questions':
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(response, reverse('stroll:login'))
        else:
            self.assertEqual(response.status_code, 200)



    # Tests for show_walk and show_question views using the unique django models ids appended to the url
    def test_walk_url_uses_walk_id(self):
        response = self.client.get(reverse('stroll:show_walk', args=[str(self.walk.id)]))
        self.assertEqual(response.status_code, 200)

    def test_question_url_uses_question_id(self):
        response = self.client.get(reverse('stroll:show_question', args=[self.question.id]))
        self.assertEqual(response.status_code, 200)


    # Tests to ensure that the views provide the correct response while logged in, if the logout view
    # is accessed by someone who is logged in, then they will be redirected to the home page
    # and automatically logged out
    def test_home_view_works(self):
        TestViewsProvideResponse.views_work_helper_except_show_walk_and_show_question(self, 'home')

    def test_about_view_works(self):
        TestViewsProvideResponse.views_work_helper_except_show_walk_and_show_question(self, 'about')

    def test_signup_view_works(self):
        TestViewsProvideResponse.views_work_helper_except_show_walk_and_show_question(self, 'signup')

    def test_create_walkt_view_works(self):
        TestViewsProvideResponse.views_work_helper_except_show_walk_and_show_question(self, 'create_walk')

    def test_user_login_view_works(self):
        TestViewsProvideResponse.views_work_helper_except_show_walk_and_show_question(self, 'login')

    def test_user_logout_view_works(self):
        TestViewsProvideResponse.views_work_helper_except_show_walk_and_show_question(self, 'logout')

    def test_my_profile_view_works(self):
        TestViewsProvideResponse.views_work_helper_except_show_walk_and_show_question(self, 'my_profile')

    def test_edit_profile_view_works(self):
        TestViewsProvideResponse.views_work_helper_except_show_walk_and_show_question(self, 'edit_profile')

    def test_my_walks_view_works(self):
        TestViewsProvideResponse.views_work_helper_except_show_walk_and_show_question(self, 'my_walks')

    def test_my_questions_view_works(self):
        TestViewsProvideResponse.views_work_helper_except_show_walk_and_show_question(self, 'my_questions')

    def test_search_walks_view_works(self):
        TestViewsProvideResponse.views_work_helper_except_show_walk_and_show_question(self, 'search_walks')

    def test_questions_view_works(self):
        TestViewsProvideResponse.views_work_helper_except_show_walk_and_show_question(self, 'questions')

    # Separate tests for non logged in users
    def test_logout_if_not_logged_in(self):
        TestViewsProvideResponse.views_work_helper_except_show_walk_and_show_question_logged_out(self, 'logout')

    def test_create_walk_if_not_logged_in(self):
        TestViewsProvideResponse.views_work_helper_except_show_walk_and_show_question_logged_out(self, 'create_walk')

    def test_home_if_not_logged_in(self):
        TestViewsProvideResponse.views_work_helper_except_show_walk_and_show_question_logged_out(self, 'home')

    def test_about_if_not_logged_in(self):
        TestViewsProvideResponse.views_work_helper_except_show_walk_and_show_question_logged_out(self, 'about')

    def test_signup_if_not_logged_in(self):
        TestViewsProvideResponse.views_work_helper_except_show_walk_and_show_question_logged_out(self, 'signup')

    def test_login_if_not_logged_in(self):
        TestViewsProvideResponse.views_work_helper_except_show_walk_and_show_question_logged_out(self, 'login')

    def test_signup_if_not_logged_in(self):
        TestViewsProvideResponse.views_work_helper_except_show_walk_and_show_question_logged_out(self, 'signup')

    def test_my_profile_if_not_logged_in(self):
        TestViewsProvideResponse.views_work_helper_except_show_walk_and_show_question_logged_out(self, 'my_profile')

    def test_edit_profile_if_not_logged_in(self):
        TestViewsProvideResponse.views_work_helper_except_show_walk_and_show_question_logged_out(self, 'edit_profile')

    def test_my_questions_if_not_logged_in(self):
        TestViewsProvideResponse.views_work_helper_except_show_walk_and_show_question_logged_out(self, 'my_questions')

    def test_my_walks_if_not_logged_in(self):
        TestViewsProvideResponse.views_work_helper_except_show_walk_and_show_question_logged_out(self, 'my_walks')

    
    # The following tests have the purpose of increasing the coverage of lines tested in views.py
    # currently "coverage report -m" shows a coverage of around 50%

class TestViewsAdditionalTests(TestCase):
    def setUp(self):
        self.user = User(username='Test user', email='Test email')
        self.user.set_password('123')
        self.user.save()
        self.user_profile = UserProfile(user=self.user)
        self.user_profile.save()

        self.client.force_login(self.user)

        self.walk1 = Walk(title='Test walk1', user=self.user, tags='test,tags', thumbnail='population_thumbnails/govan.jpg')
        self.walk1.save()
        self.walk2 = Walk(title='Test walk2', user=self.user, tags='test,tags', thumbnail='population_thumbnails/govan.jpg')
        self.walk2.save()

        self.question = Question(user=self.user_profile)
        self.question.save()

    def generate_image_for_testing(self):
        image = BytesIO()
        img = Image.new('RGB', (100, 100), color='red')
        img.save(image, format='JPG')
        image.seek(0)
        return image

    def test_home_view_context_dictionary(self):
        response = self.client.get(reverse('stroll:home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('popular_walks', response.context)
        self.assertEqual(response.context['popular_walks'][0].title, "Test walk1")
        self.assertEqual(response.context['popular_walks'][1].title, "Test walk2")

    def test_about_view_context_dictionary(self):
        response = self.client.get(reverse('stroll:about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('popular_walks', response.context)
        self.assertEqual(response.context['popular_walks'][0].title, "Test walk1")
        self.assertEqual(response.context['popular_walks'][1].title, "Test walk2")

    def test_more_signup_view_tests_form(self):

        user_input_data = {'username':'test', 'email':'test@gmail.com', 'password':'123'}
        user_profile_data = {'description':'this is a test'}

        response = self.client.post(reverse('stroll:signup'), {**user_input_data, **user_profile_data})

        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(username='test').exists())  
        self.assertTrue(UserProfile.objects.filter(user__username='test').exists())
        self.assertIn('user_form', response.context)
        self.assertIn('profile_form', response.context)
        self.assertIn('registered', response.context)

    def test_more_create_walk_view_tests_form(self):
        walk_user_input_data = {'user':self.user, 
                                'title':'test walk', 
                                'area':'govan',
                                'description':'this is a test',
                                'length':'50',
                                'difficulty':'9',
                                'tags':'test,tags',
                                'map_coordinates':'30,-20'}
        
        url = reverse('stroll:create_walk')
        response = self.client.post(url, walk_user_input_data)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Walk.objects.filter(title='test walk').exists()) 











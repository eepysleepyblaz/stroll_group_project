'''
Code based on original stroll tests from the tango with django github repository
at: https://github.com/tangowithcode/tango_with_django_2_code.git
'''


import os
import importlib
from django.urls import reverse, resolve
from django.test import TestCase
from django.conf import settings

STANDARD_FAILURE = '\n\n============\nTEST FAILED\n============\n'

class ProjectFileStructureTests(TestCase):
    # Tests for the basic file structure of the project

    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.stroll_app_dir = os.path.join(self.project_base_dir, 'stroll')

    def test_stroll_project_has_been_created(self):
        project_exists = os.path.isdir(os.path.join(self.project_base_dir, 'stroll_group_project'))
        project_urls_file_exists = os.path.isfile(os.path.join(self.project_base_dir, 'stroll_group_project', 'urls.py'))
        
        self.assertTrue(project_exists, f"{STANDARD_FAILURE} The stroll_group_project configuration directory doesn't exist.")
        self.assertTrue(project_urls_file_exists, f"{STANDARD_FAILURE} The project/urls.py file does not exist")

    def test_stroll_app_exists(self):
        stroll_exists = os.path.isdir(self.stroll_app_dir)
        is_python_package = os.path.isfile(os.path.join(self.stroll_app_dir, '__init__.py'))
        models_file_exists = os.path.isfile(os.path.join(self.stroll_app_dir, 'models.py'))
        views_file_exists = os.path.isfile(os.path.join(self.stroll_app_dir, 'views.py'))
        
        self.assertTrue(stroll_exists, f"{STANDARD_FAILURE} The stroll app directory does not exist.")
        self.assertTrue(is_python_package, f"{STANDARD_FAILURE} The stroll app directory is missing the __init__.py file.")
        self.assertTrue(models_file_exists, f"{STANDARD_FAILURE} The stroll app directory is missing the models.py file.")
        self.assertTrue(views_file_exists, f"{STANDARD_FAILURE} The stroll app directory is missing the views.py file.")
    
    def test_stroll_has_urls_module(self):
        app_urls_exists = os.path.isfile(os.path.join(self.stroll_app_dir, 'urls.py'))
        self.assertTrue(app_urls_exists, f"{STANDARD_FAILURE} The stroll app's urls.py file does not exist.")
    
    def test_is_stroll_app_in_project_settings(self):
        is_app_in_settings = 'stroll' in settings.INSTALLED_APPS
        self.assertTrue(is_app_in_settings, f"{STANDARD_FAILURE} The stroll app is missing from your setting's INSTALLED_APPS list.")


class ProjectHasCorrectTemplates(TestCase):
    # Tests for the correct template file names

    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.stroll_app_dir = os.path.join(self.project_base_dir, 'stroll')
        self.templates_dir = os.path.join(self.project_base_dir, 'templates')
        self.templates_stroll_dir = os.path.join(self.templates_dir, 'stroll')

    @staticmethod
    def template_test(self, template_name):
        file_exists = os.path.isfile(os.path.join(self.templates_stroll_dir, f'{template_name}.html'))
        return self.assertTrue(file_exists, f'{STANDARD_FAILURE} There is no {template_name}.html template')

    def test_stroll_project_has_templates_directory(self):
        directory_exists = os.path.isdir(self.templates_dir)
        self.assertTrue(directory_exists, f'{STANDARD_FAILURE} The stroll project has no directory "templates"')

    def test_templates_has_stroll_directory(self):
        directory_exists = os.path.isdir(self.templates_stroll_dir)
        self.assertTrue(directory_exists, f'{STANDARD_FAILURE} The templates directory has no directory "stroll"')

    def test_templates_has_base(self):
        ProjectHasCorrectTemplates.template_test(self, "base")

    def test_templates_has_home(self):
        ProjectHasCorrectTemplates.template_test(self, "home")

    def test_templates_has_about(self):
        ProjectHasCorrectTemplates.template_test(self, "about")

    def test_templates_has_signup(self):
        ProjectHasCorrectTemplates.template_test(self, "signup")

    def test_templates_has_login(self):
        ProjectHasCorrectTemplates.template_test(self, "login")

    def test_templates_has_create_walk(self):
        ProjectHasCorrectTemplates.template_test(self, "create_walk")

    def test_templates_has_search_walks(self):
        ProjectHasCorrectTemplates.template_test(self, "search_walks")

    def test_templates_has_questions(self):
        ProjectHasCorrectTemplates.template_test(self, "questions")

    def test_templates_has_my_profile(self):
        ProjectHasCorrectTemplates.template_test(self, "my_profile")

    def test_templates_has_selected_walk(self):
        ProjectHasCorrectTemplates.template_test(self, "show_walk")

    def test_templates_has_show_question(self):
        ProjectHasCorrectTemplates.template_test(self, "show_question")

    def test_templates_has_edit_profile(self):
        ProjectHasCorrectTemplates.template_test(self, "edit_profile")

    def test_templates_has_my_questions(self):
        ProjectHasCorrectTemplates.template_test(self, "my_questions")

    def test_templates_has_my_walks(self):
        ProjectHasCorrectTemplates.template_test(self, "my_walks")

    def test_base_starts_with_doctype(self):
        url = reverse('stroll:signup')
        response = self.client.get(url)
        self.assertTrue(response.content.decode().startswith('<!DOCTYPE html>'), f"{STANDARD_FAILURE} The base.html template does not start with '<!DOCTYPE html>'")



class ProjectViewsAndUrlsTests(TestCase):
    # Tests for correct views and urls created, they have correct mappings and
    # the views use their corresponding template

    def setUp(self):
        self.views_module = importlib.import_module('stroll.views')
        self.views_module_listing = dir(self.views_module)

    @staticmethod
    def view_and_mapping_exist_using_correct_template(self, view_name, slug=''):

        view_exists = view_name in self.views_module_listing
        is_callable = callable(getattr(self.views_module, view_name))
        self.assertTrue(view_exists, f'{STANDARD_FAILURE} There is no view "{view_name}"')
        self.assertTrue(is_callable, f'{STANDARD_FAILURE} The view "{view_name}" should be a function')

        if view_name == 'show_walk':
            url = reverse(f'stroll:{view_name}', kwargs={'walk_name_slug': 'example-walk'})

        elif view_name == 'show_question':
            url = reverse(f'stroll:{view_name}', kwargs={'question_slug': 'example-question'})

        else:
            url = reverse(f'stroll:{view_name}')

        match = resolve(url)
        self.assertEquals(match.func, getattr(self.views_module, view_name), f'{STANDARD_FAILURE} The view "{view_name}" is not mapped correctly')

        template_path = f'stroll/{view_name}.html'
        response = self.client.get(url)
        self.assertTemplateUsed(response, template_path, f'{STANDARD_FAILURE} The view "{view_name}" does not use a template or a correct template')

    
    def test_home_view_exisits(self):
        ProjectViewsAndUrlsTests.view_and_mapping_exist_using_correct_template(self, 'home')

    def test_about_view_exisits(self):
        ProjectViewsAndUrlsTests.view_and_mapping_exist_using_correct_template(self, 'about')

    def test_signup_view_exisits(self):
        ProjectViewsAndUrlsTests.view_and_mapping_exist_using_correct_template(self, 'signup')

    def test_create_walk_view_exisits(self):
        ProjectViewsAndUrlsTests.view_and_mapping_exist_using_correct_template(self, 'create_walk')

    def test_login_view_exisits(self):
        ProjectViewsAndUrlsTests.view_and_mapping_exist_using_correct_template(self, 'login')

    def test_my_profile_view_exisits(self):
        ProjectViewsAndUrlsTests.view_and_mapping_exist_using_correct_template(self, 'my_profile')

    def test_edit_profile_view_exisits(self):
        ProjectViewsAndUrlsTests.view_and_mapping_exist_using_correct_template(self, 'edit_profile')

    def test_my_walks_view_exisits(self):
        ProjectViewsAndUrlsTests.view_and_mapping_exist_using_correct_template(self, 'my_walks')

    def test_my_questions_view_exisits(self):
        ProjectViewsAndUrlsTests.view_and_mapping_exist_using_correct_template(self, 'my_questions')

    def test_search_walks_view_exisits(self):
        ProjectViewsAndUrlsTests.view_and_mapping_exist_using_correct_template(self, 'search_walks')

    def test_show_walk_view_exisits(self):
        ProjectViewsAndUrlsTests.view_and_mapping_exist_using_correct_template(self, 'show_walk')

    def test_questions_view_exisits(self):
        ProjectViewsAndUrlsTests.view_and_mapping_exist_using_correct_template(self, 'questions')

    def test_show_question_view_exisits(self):
        ProjectViewsAndUrlsTests.view_and_mapping_exist_using_correct_template(self, 'show_question')
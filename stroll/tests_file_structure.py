'''
Code based on original stroll tests from the tango with django github repository
at: https://github.com/tangowithcode/tango_with_django_2_code.git
'''


import os
import importlib
from django.urls import reverse
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
    def template_test(self, name):
        file_exists = os.path.isfile(os.path.join(self.templates_stroll_dir, f'{name}.html'))
        return self.assertTrue(file_exists, f'{STANDARD_FAILURE} There is no {name}.html template')

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
        ProjectHasCorrectTemplates.template_test(self, "selected_walk")

    def test_templates_has_show_question(self):
        ProjectHasCorrectTemplates.template_test(self, "show_question")

    def test_templates_has_edit_profile(self):
        ProjectHasCorrectTemplates.template_test(self, "edit_profile")

    def test_templates_has_my_questions(self):
        ProjectHasCorrectTemplates.template_test(self, "my_questions")

    def test_templates_has_my_walks(self):
        ProjectHasCorrectTemplates.template_test(self, "my_walks")




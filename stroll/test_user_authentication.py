'''
Code based on original tests from the tango with django github repository
at: https://github.com/tangowithcode/tango_with_django_2_code.git
'''


import os
import importlib
from django.urls import reverse, resolve
from django.test import TestCase
from django.conf import settings

STANDARD_FAILURE = '\n\n============\nTEST FAILED\n============\n'

class MediaAndStaticDirectoryTests(TestCase):
    # Tests for the basic file structure of the project

    def setUp(self):
        self.project_base_dir = os.getcwd()

    def test_authentication_apps_configured_in_project_settings(self):
        is_django_contrib_auth_in_settings = 'django.contrib.auth' in settings.INSTALLED_APPS
        is_django_contrib_contenttypes_in_settings = 'django.contrib.contenttypes' in settings.INSTALLED_APPS
        self.assertTrue(is_django_contrib_auth_in_settings, f"{STANDARD_FAILURE} The django.contrib.auth app is missing from your setting's INSTALLED_APPS list.")
        self.assertTrue(is_django_contrib_contenttypes_in_settings, f"{STANDARD_FAILURE} The django.contrib.contenttypes app is missing from your setting's INSTALLED_APPS list.")

    
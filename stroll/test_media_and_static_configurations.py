'''
Code based on original tests from the tango with django github repository
at: https://github.com/tangowithcode/tango_with_django_2_code.git

Tests might take 20-30 seconds to complete.
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
        self.media_dir = os.path.join(self.project_base_dir, 'media')
        self.static_dir = os.path.join(self.project_base_dir, 'static')

    def test_media_dir_has_correct_subdirectories(self):
        media_dir_exists = os.path.isdir(self.media_dir)
        media_gallery_dir_exists = os.path.isdir(os.path.join(self.media_dir, 'walk_galleries'))
        media_profile_pictures_dir_exists = os.path.isdir(os.path.join(self.media_dir, 'profile_pictures'))
        media_walk_thumbnails_dir_exists = os.path.isdir(os.path.join(self.media_dir, 'walk_thumbnails'))

        self.assertTrue(media_dir_exists, f"{STANDARD_FAILURE}The media directory does not exist or is not in the correct location.")
        self.assertTrue(media_gallery_dir_exists, f"{STANDARD_FAILURE}The media/gallery directory does not exist or is not in the correct location.")
        self.assertTrue(media_profile_pictures_dir_exists, f"{STANDARD_FAILURE}The media/profile_pictures directory does not exist or is not in the correct location.")
        self.assertTrue(media_walk_thumbnails_dir_exists, f"{STANDARD_FAILURE}The media/walk_thumbnails directory does not exist or is not in the correct location.")

    def test_static_dir_has_correct_subdirectories(self):
        static_dir_exists = os.path.isdir(self.static_dir)
        static_css_dir_exists = os.path.isdir(os.path.join(self.static_dir, 'css'))
        static_images_dir_exists = os.path.isdir(os.path.join(self.static_dir, 'images'))

        self.assertTrue(static_dir_exists, f"{STANDARD_FAILURE}The static directory does not exist or is not in the correct location.")
        self.assertTrue(static_css_dir_exists, f"{STANDARD_FAILURE}The static/css directory does not exist or is not in the correct location.")
        self.assertTrue(static_images_dir_exists, f"{STANDARD_FAILURE}The static/images directory does not exist or is not in the correct location.")

    def test_static_directory_configuration(self):
        static_dir_exists = 'STATIC_DIR' in dir(settings)
        self.assertTrue(static_dir_exists, f"{STANDARD_FAILURE}The settings.py module has no 'STATIC_DIR' variable declared and initialised.")

        expected_path = os.path.normpath(self.static_dir)
        static_path = os.path.normpath(settings.STATIC_DIR)
        self.assertEqual(expected_path, static_path, f"{STANDARD_FAILURE}STATIC_DIR does not have the correct value.")

        staticfiles_dirs_exists = 'STATICFILES_DIRS' in dir(settings)
        self.assertTrue(staticfiles_dirs_exists, f"{STANDARD_FAILURE}The STATICFILES_DIRS setting does not exist in the settings.py module.")
        self.assertEqual([static_path], settings.STATICFILES_DIRS, f"{STANDARD_FAILURE}The STATICFILES_DIR setting is not properly configured.")

        static_url_exists = 'STATIC_URL' in dir(settings)
        self.assertTrue(static_url_exists, f"{STANDARD_FAILURE}The STATIC_URL variable does not exist.")
        self.assertEqual('/static/', settings.STATIC_URL, f"{STANDARD_FAILURE}STATIC_URL has not been declared correctly.")


    def test_media_directory_configuration(self):
        media_dir_exists = 'MEDIA_DIR' in dir(settings)
        self.assertTrue(media_dir_exists, f"{STANDARD_FAILURE}The settings.py module has no 'MEDIA_DIR' variable declared and initialised.")

        expected_path = os.path.normpath(self.media_dir)
        media_path = os.path.normpath(settings.MEDIA_DIR)
        self.assertEqual(expected_path, media_path, f"{STANDARD_FAILURE}MEDIA_DIR does not have the correct value.")

        media_root_exists = 'MEDIA_ROOT' in dir(settings)
        media_root_path = os.path.normpath(settings.MEDIA_ROOT)
        self.assertTrue(media_root_exists, f"{STANDARD_FAILURE}The MEDIAFILES_DIRS setting does not exist in the settings.py module.")
        self.assertEqual(media_path, media_root_path, f"{STANDARD_FAILURE}MEDIA_ROOT and MEDIA_DIR should be equal.")

        media_url_exists = 'MEDIA_URL' in dir(settings)
        self.assertTrue(media_url_exists, f"{STANDARD_FAILURE}The MEDIA_URL variable does not exist.")
        self.assertEqual('/media/', settings.MEDIA_URL, f"{STANDARD_FAILURE}MEDIA_URL has not been declared correctly.")

    def test_context_processor_for_media_has_been_configured(self):
        context_processors = settings.TEMPLATES[0]['OPTIONS']['context_processors']
        self.assertTrue('django.template.context_processors.media' in context_processors, f"{STANDARD_FAILURE}The template context processor for media files has not been added in settings.py of the project.")
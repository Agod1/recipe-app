from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from core import models


class ModelTest(TestCase):

    def sample_user(email='test@recipe.app', password='testpass'):
        """Create a sample user"""
        return get_user_model().objects.create_user(email, password)

    def test_create_user_with_email_successful(self):
        '''Test creating a new user with email is successful'''
        email = 'test@recipe.app'
        password = '123456'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_user_email_is_normalized(self):
        '''Test that a new user email is normalized'''
        email = 'test@recipe.App'
        password = '123456'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email.lower())


    def test_user_email_is_provided(self):
        '''Test that a new user email is provided'''
        email = None
        password = '123456'
        with self.assertRaises(ValueError):
            user = get_user_model().objects.create_user(
                email=email,
                password=password
            )


    def _test_user_email_is_valid(self):
        '''Test that a new user email is valid'''
        email = 'testrecipe.App'
        password = '123456'
        with self.assertRaises(ValidationError):
            user = get_user_model().objects.create_user(
                email=email,
                password=password
            )


    def test_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@recipe.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user = get_user_model().objects.create_user(
                'test@recipe.com',
                'test123'
            ),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)

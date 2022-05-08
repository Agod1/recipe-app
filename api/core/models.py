import email
from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_args):
        '''Create and save new user'''
        if not email: raise ValueError
        validate_email(email)
        user = self.model(email=self.normalize_email(email), **extra_args)
        user.set_password(password)
        user.save(self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    '''Custom user model that uses email instead of username'''
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

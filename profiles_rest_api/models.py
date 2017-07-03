from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserProfileManager(BaseUserManager):
    """
    Helps Django work with our custom user model
    """

    def create_user(self, email, name, password=None):
        """
        Creates a new user profile object
        """
        if not email:
            raise ValueError('Users must have an email address.')

        # convert email string to lowercase
        email = self.normalize_email(email)

        user = self.model(email=email, name=name)

        # The set_password method encrypts the user password
        # And save it in the database as a hash
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):

        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Represents a user profile inside our system
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_short_name(self):
        return self.name

    def get_full_name(self):
        return self.name

    def __str__(self):
        return self.email

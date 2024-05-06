from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

# User manager for Account model
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password = None):
        if not email:
            raise ValueError("You must have an email silly")
        if not username:
            raise ValueError("You must have a username brother")

        user = self.model(
            email = self.normalize_email(email),
            username = username
            )

        user.set_password(password)
        user.save(using = self._db)
        return user

    # Method to create a superuser
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

# User model for accounts
class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name = 'email', max_length = 60, unique = True)
    username = models.CharField(max_length = 30, unique = True)
    date_joined = models.DateTimeField(verbose_name = 'date joined', auto_now_add = True)
    last_login = models.DateTimeField(verbose_name = 'last login', auto_now = True)
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    # String representation of the Account model
    def __str__(self):
        return self.email 

    # Method to check if user has specific permissions
    def has_perm(self, perm, obj = None):
        return self.is_admin

    # Method to check if user has permissions for a specific module
    def has_module_perms(self, app_label):
        return True

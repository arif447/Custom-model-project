from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.
class CreateUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('You have must Email')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def create_employee(self, email, password):
        user = self.create_user(email, password)
        user.is_employee = True
        user.save(using=self._db)
        return user

class CreateUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=100)
    is_employee = models.BooleanField('is_employee', default=False)
    is_staff = models.BooleanField('is_staff', default=False)
    is_active = models.BooleanField(default=True)

    objects = CreateUserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

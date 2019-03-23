from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,
                                        BaseUserManager,
                                        PermissionsMixin,)

class UserManager(BaseUserManager): #So that we can use get_user_model
    def create_user(self,email,password):
        """Creates a New user"""
        user = self.model(email = self.normalize_email(email))
        user.set_password(password)
        user.save(using = self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'

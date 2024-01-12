from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
	def create_user(self, email, password=None, **kwargs):
		if not email:
			raise ValueError("You nedd enter email")

		user = self.model(
			email=self.normalize_email(email),
			**kwargs
		)

		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, email, password=None, **kwargs):
		user = self.create_user(email=email, password=password, **kwargs)
		user.is_admin = True
		user.is_staff = True
		user.save()
		return user


# Create your models here.
class User(AbstractUser):
	email = models.EmailField(
		unique=True,
		max_length=255,
		blank=False
	)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)
	username = models.CharField(max_length=16)

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ["username"]

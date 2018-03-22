from django.db import models
from django.contrib.auth.models import (
	AbstractBaseUser,
	BaseUserManager,
	PermissionsMixin
)
from django.utils import timezone
import os




# Create your models here.
class UserManager(BaseUserManager):
	def create_user(self, email, password=None):
		if not email:
			raise ValueError("users must have a email address")
		user = self.model(
			email = self.normalize_email(email),
		)
		user.set_password(password)
		user.save()
		return user
	
	def create_superuser(self, email, password):
		user = self.create_user(
			email,
			password
		)
		user.is_staff = True
		user.is_superuser = True
		user.save()
		return user

class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(
					verbose_name='email address',
					max_length=255,
					unique=True)
	display_name = models.CharField(default='',max_length=40)
	full_name = models.CharField(default='',max_length=40)
	bio = models.TextField(default='')
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	joined_at = models.DateTimeField(default=timezone.now)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELD = ['email','full_name','bio','image','is_active','is_staff','joined_at']



	def __str__(self):
		return self.email

class ProfileImage(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,
								primary_key=True, related_name='profile_image')
	image = models.ImageField(upload_to='avatars/',null=True)

	def __str__(self):
		return "{} {}".format(self.user, self.image)
	
	


		

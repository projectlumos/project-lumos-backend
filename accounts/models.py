from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserInfo(models.Model):
	"""
	A Separate class to store additional information 
	about the user.
	"""
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	email = models.EmailField(unique=True)


	def __str__(self):
		return self.user
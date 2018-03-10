from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserInfo(models.Model):
	"""
	A Separate class to store additional information 
	about the user.

	"""
	lumos_user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return '{username}'.format(username=self.lumos_user.username)

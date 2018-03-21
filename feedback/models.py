from django.db import models
from django.contrib.auth.models import User
from courses.utils.modelsutils import RowInformation

# Create your models here.

class Feedback(RowInformation):
	"""
	class to store feedback information.
	"""
	user = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
	text = models.TextField()

	
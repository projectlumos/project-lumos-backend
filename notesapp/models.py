import courses
from django.db import models
from django.contrib.auth.models import User
from courses.utils.modelsutils import RowInformation
from datetime import date
from django.utils import timezone


# Create your models here.


class Notes(RowInformation):
	"""
	This is the base class for Notes models.
	It stores all the attribute common to all
	the child classes.

	"""
	user = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
	title = models.CharField(max_length=120)
	content = models.TextField()
	created_date = models.DateField(default=timezone.now().date())
	date_modified = models.DateTimeField(auto_now=True,auto_now_add=False,null=True)

	class Meta:
		abstract = True


class KnowledgeBaseNotes(Notes):
	"""
	This model will handle the notes for KnowledgeBase Resource.
	It will inherit from base class which is notes.

	"""

	resource = models.ForeignKey('courses.KnowledgeBase', on_delete=models.CASCADE)

	def __str__(self):
		return self.resource.title


class SoftSkillsDataNotes(Notes):
	"""
	This model will handle the notes for SoftSkillsData Resource.
	It will inherit from base class which is notes.

	"""

	resource = models.ForeignKey('courses.SoftSkillsData', on_delete=models.CASCADE)

	def __str__(self):
		return self.resource.title


class RandomDataNotes(Notes):
	"""
	This model will handle the notes for RandomData Resource.
	It will inherit from base class which is notes.

	"""

	resource = models.ForeignKey('courses.RandomData', on_delete=models.CASCADE)

	def __str__(self):
		return self.resource.title


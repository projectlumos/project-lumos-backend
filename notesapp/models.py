from django.db import models
from django.db import transaction
from django.contrib.auth.models import User
from courses.models import(KnowledgeBase,
						   SoftSkillsData,
						   RandomData)
from courses.utils.modelsutils import RowInformation
from courses.utils.modelsutils import pl_custom_slugify

# Create your models here.


class Notes(RowInformation):
	"""
	This is the base class for Notes models.
	It stores all the attribute common to all
	the child classes.

	"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=120)
	content = models.TextField()
	
	class Meta:
		abstract = True


class KnowledgeBaseNotes(Notes):
	"""
	This model will handle the notes for KnowledgeBase Resource.
	It will inherit from base class which is notes.

	"""

	resource = models.ForeignKey(KnowledgeBase, on_delete=models.CASCADE)
	slug = models.SlugField(unique=True)

	def save(self, *args, **kwargs):

		self.title = self.title.title() if self.title else self.title

		if not self.slug:
		    # if slug doesn't exist pass the source_field and suffix=False to custom_slugify function
		    self.slug = pl_custom_slugify(source_field=self.title, suffix=False)

		try:
			"""
			While saving, it we have a duplicate combination of name and slug
			Since we have added an IntegrityError check, we will have an exception raised
			"""
			#This will prevent the purposefully-thrown exception from breaking the entire unittest's transaction.
			with transaction.atomic():
			# since unique combination of source_field and slug exists, call save method
				super(KnowledgeBaseNotes, self).save(*args, **kwargs)

		except IntegrityError:
			"""
			after catching the exception, we will generate another slug but this time we will
			suffix  it with a random string at the end of the slug to make it unique and try saving it again
			"""

			# since unique combination of source_field and slug doesn't exist,
			# pass suffix=True to add random_str to make it unique
			self.slug = pl_custom_slugify(source_field=self.title, suffix=True)
			super(KnowledgeBaseNotes, self).save(*args, **kwargs)

	def __str__(self):
		return '{title}-{slug}'.format(title=self.title, slug=self.slug)


class SoftSkillsDataNotes(Notes):
	"""
	This model will handle the notes for SoftSkillsData Resource.
	It will inherit from base class which is notes.

	"""

	resource = models.ForeignKey(SoftSkillsData, on_delete=models.CASCADE)
	slug = models.SlugField(unique=True)

	def save(self, *args, **kwargs):

		self.title = self.title.title() if self.title else self.title

		if not self.slug:
		    # if slug doesn't exist pass the source_field and suffix=False to custom_slugify function
			self.slug = pl_custom_slugify(source_field=self.title, suffix=False)

		try:
			"""
			While saving, it we have a duplicate combination of name and slug
			Since we have added an IntegrityError check, we will have an exception raised
			"""
			#This will prevent the purposefully-thrown exception from breaking the entire unittest's transaction.
			with transaction.atomic():
			    # since unique combination of source_field and slug exists, call save method
				super(SoftSkillsDataNotes, self).save(*args, **kwargs)

		except IntegrityError:
			"""
			after catching the exception, we will generate another slug but this time we will
			suffix  it with a random string at the end of the slug to make it unique and try saving it again
			"""

			# since unique combination of source_field and slug doesn't exist,
			# pass suffix=True to add random_str to make it unique
			self.slug = pl_custom_slugify(source_field=self.title, suffix=True)
			super(SoftSkillsDataNotes, self).save(*args, **kwargs)

	def __str__(self):
		return '{title}-{slug}'.format(title=self.title, slug=self.slug)


class RandomDataNotes(Notes):
	"""
	This model will handle the notes for RandomData Resource.
	It will inherit from base class which is notes.

	"""

	resource = models.ForeignKey(RandomData, on_delete=models.CASCADE)
	slug = models.SlugField(unique=True)

	def save(self, *args, **kwargs):

		self.title = self.title.title() if self.title else self.title

		if not self.slug:
		    # if slug doesn't exist pass the source_field and suffix=False to custom_slugify function
			self.slug = pl_custom_slugify(source_field=self.title, suffix=False)

		try:
			"""
			While saving, it we have a duplicate combination of name and slug
			Since we have added an IntegrityError check, we will have an exception raised
			"""
			#This will prevent the purposefully-thrown exception from breaking the entire unittest's transaction.
			with transaction.atomic():
			    # since unique combination of source_field and slug exists, call save method
				super(RandomDataNotes, self).save(*args, **kwargs)

		except IntegrityError:
			"""
			after catching the exception, we will generate another slug but this time we will
			suffix  it with a random string at the end of the slug to make it unique and try saving it again
			"""

			# since unique combination of source_field and slug doesn't exist,
			# pass suffix=True to add random_str to make it unique
			self.slug = pl_custom_slugify(source_field=self.title, suffix=True)
			super(RandomDataNotes, self).save(*args, **kwargs)

	def __str__(self):
		return '{title}-{slug}'.format(title=self.title, slug=self.slug)

from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from courses.utils.constants import skill_levels, data_types, language_for, domain_for
from django.db import IntegrityError
from courses.utils import modelsutils
from courses.utils.modelsutils import RowInformation

# Create your models here.


'''
PLEASE MAKE CHANGES FOR THE REST OF THE DJANGO PROJECT WRT COMMENTS

USE THIS

# this is a comment
how_to = "write comments"

INSTEAD OF

how_not = "to write comments" #coz this is simply not readable, you read top to bottom and left to right

this way, you are first reading the code, then the comment, but again you have to read the code coz of some new info
available due to comment

'''


def custom_slugify(source_field, suffix=False):
    """
    Using django util methods create a slug.
    Append a random string at the end of the slug if necessary for making it unique
    """
    new_slug = slugify(source_field)  # slugify the source_field passed to the function

    if suffix:
        # get a random string of length 10
        random_str = get_random_string(length=10)

        # the new_slug and random_str is concatenated
        new_slug = "{0}-{1}".format(new_slug, random_str)

    return new_slug


class Language(models.Model):
    """
    It refers to the various languages in technical skills and soft skills context.
    This class consists of language attributes such as
    language_name, slug, description and icon
    """
    language_name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    # if no site_url, store empty string
    site_url = models.URLField(null=False, blank=True)

    # if no description, store empty string
    description = models.TextField(null=False, blank=True)

    # if no icon_url, store empty string
    icon = models.URLField(null=False, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # if slug doesn't exist pass the source_field and suffix=False to custom_slugify function
            self.slug = modelsutils.custom_slugify(source_field=self.language_name, suffix=False)

        try:
            """
            While saving, it we have a duplicate combination of name and slug
            Since we have added an IntegrityError check, we will have an exception raised
            """
            super(Language, self).save(
                *args, **kwargs)  # since unique combination of source_field and slug exists, call save method

        except IntegrityError:
            """
            after catching the exception, we will generate another slug but this time we will
            suffix  it with a random string at the end of the slug to make it unique and try saving it again
            """
            # since unique combination of source_field and slug doesn't exist, pass suffix=True to add random_str to make it unique
            self.slug = modelsutils.custom_slugify(source_field=self.language_name, suffix=True)
            super(Language, self).save(*args, **kwargs)

    def __str__(self):
        return '{name}-{slug}'.format(name=self.language_name, slug=self.slug)

    class Meta:
        # checks whether the combination of two fields is unique
        unique_together = ('language_name', 'slug')


class Domain(models.Model):
    """
    It refers to the various domains in the technical skills and soft skills context.
    This class consists of domain attributes such as
    domain_name, slug, description and icon
    """
    domain_name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    # if no description, store empty string
    description = models.TextField(null=False, blank=True)

    # if no icon_url, store empty string
    icon = models.URLField(null=False, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = modelsutils.custom_slugify(source_field=self.domain_name, suffix=False)

        try:
            """
            While saving, it we have a duplicate combination of name and slug
            Since we have added an IntegrityError check, we will have an exception raised
            """
            # since unique combination of source_field and slug exists, call save method
            super(Domain, self).save(*args, **kwargs)

        except IntegrityError:
            """
            after catching the exception, we will generate another slug but this time we will
            suffix  it with a random string at the end of the slug to make it unique and try saving it again
            """
            # since unique combination of source_field and slug doesn't exist, pass suffix=True to add random_str to make it unique
            self.slug = modelsutils.custom_slugify(source_field=self.domain_name, suffix=True)
            super(Domain, self).save(*args, **kwargs)

    def __str__(self):
        return '{name}-{slug}'.format(name=self.domain_name, slug=self.slug)

    class Meta:
        # checks whether the combination of two fields is unique
        unique_together = ('domain_name', 'slug')


class SoftSkills(models.Model):
    """
    This class refers to softskills categories.
    This class consists of softskills attributes such as
    soft_skill_category, slug, description and icon
    """
    soft_skill_category = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    # if no description, store empty string
    description = models.TextField(null=False, blank=True)

    # if no icon_url, store empty string
    icon = models.URLField(null=False, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = modelsutils.custom_slugify(source_field=self.soft_skill_category, suffix=False)

        try:
            """
            While saving, it we have a duplicate combination of name and slug
            Since we have added an IntegrityError check, we will have an exception raised
            """
            # since unique combination of source_field and slug exists, call save method
            super(SoftSkills, self).save(*args, **kwargs)

        except IntegrityError:
            """
            after catching the exception, we will generate another slug but this time we will
            suffix  it with a random string at the end of the slug to make it unique and try saving it again
            """
            # since unique combination of source_field and slug doesn't exist, pass suffix=True to add random_str to make it unique
            self.slug = modelsutils.custom_slugify(source_field=self.soft_skill_category, suffix=True)
            super(SoftSkills, self).save(*args, **kwargs)

    def __str__(self):
        return '{name}-{slug}'.format(name=self.soft_skill_category, slug=self.slug)

    class Meta:
        # checks whether the combination of two fields is unique
        unique_together = ('soft_skill_category', 'slug')


class SoftSkillsData(RowInformation):
    """
    This class refers to SoftSkills resources.
    It consists of attributes such as soft_skill, title, description, slug, link_url,
    data_type and paid
    """
    soft_skill = models.ManyToManyField(SoftSkills, related_name='soft_skills')
    title = models.CharField(max_length=100, null=False, blank=False)

    # if no description, store empty string
    description = models.TextField(null=False, blank=True)
    slug = models.SlugField(unique=True)
    link_url = models.URLField(null=False, blank=False, unique=True)

    # indicates the type of data, video, blog, tutorial, course or others
    data_type = models.CharField(max_length=2, choices=data_types)

    # indicates whether the resource is paid or not
    paid = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = modelsutils.custom_slugify(source_field=self.title, suffix=False)

        try:
            """
            While saving, it we have a duplicate combination of name and slug
            Since we have added an IntegrityError check, we will have an exception raised
            """
            # since unique combination of source_field and slug exists, call save method
            super(SoftSkillsData, self).save(*args, **kwargs)

        except IntegrityError:
            """
            after catching the exception, we will generate another slug but this time we will
            suffix  it with a random string at the end of the slug to make it unique and try saving it again
            """
            # since unique combination of source_field and slug doesn't exist, pass suffix=True to add random_str to make it unique
            self.slug = modelsutils.custom_slugify(source_field=self.title, suffix=True)
            super(SoftSkillsData, self).save(*args, **kwargs)

    def __str__(self):
        return '{name}-{slug}'.format(name=self.title, slug=self.slug)

    class Meta:
        ordering = ['-modified_at', '-created_at']
        # checks whether the combination of two fields is unique
        unique_together = ('title', 'slug')


class KnowledgeBase(RowInformation):
    """
    This class is used to maintain attributes which are common to both the
    Video class and ExternalLink class. It inherits from RowInformation class
    """
    title = models.CharField(max_length=100, null=False, blank=False)

    # if no description, store empty string
    description = models.TextField(null=False, blank=True)
    slug = models.SlugField(unique=True)

    # skill level required to understand the resource
    skill_level = models.CharField(max_length=2, choices=skill_levels)

    # indicates the type of data, video, blog, tutorial, course or others
    data_type = models.CharField(max_length=2, choices=data_types)

    # languages associated with the resource
    languages = models.ManyToManyField(Language, related_name='%(class)s_languages', blank=True,
                                        validators=[validate_language])

    # domains associated with the resource
    domains = models.ManyToManyField(Domain, related_name='%(class)s_domains', blank=True,
                                        validators=[validate_domain])
    link_url = models.URLField(null=False, blank=False, unique=True)

    # indicates whether the resource is paid or not
    paid = models.BooleanField(default=False)

    # indicates if it's a project resource or not
    project = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = modelsutils.custom_slugify(source_field=self.title, suffix=False)

        try:
            """
            While saving, it we have a duplicate combination of name and slug
            Since we have added an IntegrityError check, we will have an exception raised
            """
            super(KnowledgeBase, self).save(*args, **kwargs)

        except IntegrityError:
            """
            after catching the exception, we will generate another slug but this time we will
            suffix  it with a random string at the end of the slug to make it unique and try saving it again
            """
            self.slug = modelsutils.custom_slugify(source_field=self.title, suffix=True)
            super(KnowledgeBase, self).save(*args, **kwargs)

    def validate_language(value):
        validate_language.language = value

    def validate_domain(value):
        validate_domain.domain = value
        if validate_language.language is None and validate_domain.domain is None:
            raise ValidationError(
            _('both languages and domains cannot be none'),
        )

    def __str__(self):
        return self.slug

    class Meta:
        abstract = True  # used as a base class for other models
        ordering = ['-modified_at', '-created_at']
        unique_together = ('title', 'slug')  # checks whether the combination of two fields is unique


class RandomData(RowInformation):
    """
    This class refers to all the random resources.
    It consists of attributes like title, description, slug, link_url,
    data_type and paid
    """
    title = models.CharField(max_length=100, null=False, blank=False)

    # if no description, store empty string
    description = models.TextField(null=False, blank=True)
    slug = models.SlugField(unique=True)
    link_url = models.URLField(null=False, blank=False, unique=True)

    # indicates the type of data, video, blog, tutorial, course or others
    data_type = models.CharField(max_length=2, choices=data_types)

    # indicates whether the resource is paid or not
    paid = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = modelsutils.custom_slugify(source_field=self.title, suffix=False)

        try:
            """
            While saving, it we have a duplicate combination of name and slug
            Since we have added an IntegrityError check, we will have an exception raised
            """
            # since unique combination of source_field and slug exists, call save method
            super(RandomData, self).save(*args, **kwargs)

        except IntegrityError:
            """
            after catching the exception, we will generate another slug but this time we will
            suffix  it with a random string at the end of the slug to make it unique and try saving it again
            """
            # since unique combination of source_field and slug doesn't exist, pass suffix=True to add random_str to make it unique
            self.slug = modelsutils.custom_slugify(source_field=self.title, suffix=True)
            super(RandomData, self).save(*args, **kwargs)

    def __str__(self):
        return '{name}-{slug}'.format(name=self.title, slug=self.slug)

    class Meta:
        ordering = ['-modified_at', '-created_at']
        # checks whether the combination of two fields is unique
        unique_together = ('title', 'slug')

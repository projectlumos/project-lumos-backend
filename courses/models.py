from django.db import models
from django.db import transaction
from courses.utils.constants import SKILL_LEVELS, DATA_TYPES
from django.db import IntegrityError
from courses.utils.modelsutils import pl_custom_slugify
from courses.utils.modelsutils import RowInformation

# Create your models here.


class Language(models.Model):
    """
    It refers to the various languages in technical skills and soft skills context.
    This class consists of language attributes such as
    language_name, slug, description and icon
    """
    language_name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    # if no site_url, store empty null frontend will handle
    site_url = models.URLField(null=True, blank=True)

    # if no description, store empty null frontend will handle
    description = models.TextField(null=True, blank=True)

    # if no icon_url, store empty null frontend will handle
    icon = models.URLField(null=True, blank=True)

    def save(self, *args, **kwargs):

        self.language_name = self.language_name.title() if self.language_name else self.language_name

        if not self.slug:
            # if slug doesn't exist pass the source_field and suffix=False to custom_slugify function
            self.slug = pl_custom_slugify(source_field=self.language_name, suffix=False)

        try:
            """
            While saving, it we have a duplicate combination of name and slug
            Since we have added an IntegrityError check, we will have an exception raised
            """
            #This will prevent the purposefully-thrown exception from breaking the entire unittest's transaction.
            with transaction.atomic():
                # since unique combination of source_field and slug exists, call save method
                super(Language, self).save(*args, **kwargs)

        except IntegrityError:
            """
            after catching the exception, we will generate another slug but this time we will
            suffix  it with a random string at the end of the slug to make it unique and try saving it again
            """

            # since unique combination of source_field and slug doesn't exist,
            # pass suffix=True to add random_str to make it unique
            self.slug = pl_custom_slugify(source_field=self.language_name, suffix=True)
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
    description = models.TextField(null=True, blank=True)
    icon = models.URLField(null=True, blank=True)

    def save(self, *args, **kwargs):

        self.domain_name = self.domain_name.title() if self.domain_name else self.domain_name

        if not self.slug:
            self.slug = pl_custom_slugify(source_field=self.domain_name, suffix=False)

        try:
            """
            While saving, it we have a duplicate combination of name and slug
            Since we have added an IntegrityError check, we will have an exception raised
            """
            #This will prevent the purposefully-thrown exception from breaking the entire unittest's transaction.
            with transaction.atomic():
                # since unique combination of source_field and slug exists, call save method
                super(Domain, self).save(*args, **kwargs)

        except IntegrityError:
            """
            after catching the exception, we will generate another slug but this time we will
            suffix  it with a random string at the end of the slug to make it unique and try saving it again
            """
            self.slug = pl_custom_slugify(source_field=self.domain_name, suffix=True)
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
    description = models.TextField(null=True, blank=True)
    # if no icon_url, store empty string
    icon = models.URLField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # title casing
        self.soft_skill_category = self.soft_skill_category.title() if self.soft_skill_category \
            else self.soft_skill_category

        if not self.slug:
            self.slug = pl_custom_slugify(source_field=self.soft_skill_category, suffix=False)

        try:
            """
            While saving, it we have a duplicate combination of name and slug
            Since we have added an IntegrityError check, we will have an exception raised
            """
            #This will prevent the purposefully-thrown exception from breaking the entire unittest's transaction.
            with transaction.atomic():
                # since unique combination of source_field and slug exists, call save method
                super(SoftSkills, self).save(*args, **kwargs)

        except IntegrityError:
            """
            after catching the exception, we will generate another slug but this time we will
            suffix  it with a random string at the end of the slug to make it unique and try saving it again
            """
            self.slug = pl_custom_slugify(source_field=self.soft_skill_category, suffix=True)
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
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True)
    link_url = models.URLField(null=False, blank=False, unique=True)

    # indicates the type of data, video, blog, tutorial, course or others
    data_type = models.CharField(max_length=2, choices=DATA_TYPES)

    # indicates whether the resource is paid or not
    paid = models.BooleanField(default=False)

    def save(self, *args, **kwargs):

        self.title = self.title.title() if self.title else self.title

        if not self.slug:
            self.slug = pl_custom_slugify(source_field=self.title, suffix=False)

        try:
            """
            While saving, it we have a duplicate combination of name and slug
            Since we have added an IntegrityError check, we will have an exception raised
            """
            #This will prevent the purposefully-thrown exception from breaking the entire unittest's transaction.
            with transaction.atomic():
                # since unique combination of source_field and slug exists, call save method
                super(SoftSkillsData, self).save(*args, **kwargs)

        except IntegrityError:
            """
            after catching the exception, we will generate another slug but this time we will
            suffix  it with a random string at the end of the slug to make it unique and try saving it again
            """
            self.slug = pl_custom_slugify(source_field=self.title, suffix=True)
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
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True)

    # skill level required to understand the resource
    skill_level = models.CharField(max_length=2, choices=SKILL_LEVELS)

    # indicates the type of data, video, blog, tutorial, course or others
    data_type = models.CharField(max_length=2, choices=DATA_TYPES)

    # languages associated with the resource
    languages = models.ManyToManyField(Language, related_name='%(class)s_languages', blank=True)

    # domains associated with the resource
    domains = models.ManyToManyField(Domain, related_name='%(class)s_domains', blank=True)
    link_url = models.URLField(null=False, blank=False, unique=True)

    # indicates whether the resource is paid or not
    paid = models.BooleanField(default=False)

    # indicates if it's a project resource or not
    project = models.BooleanField(default=False)

    def save(self, *args, **kwargs):

        self.title = self.title.title() if self.title else self.title

        if not self.slug:
            self.slug = pl_custom_slugify(source_field=self.title, suffix=False)

        try:
            """
            While saving, it we have a duplicate combination of name and slug
            Since we have added an IntegrityError check, we will have an exception raised
            """
            #This will prevent the purposefully-thrown exception from breaking the entire unittest's transaction.
            with transaction.atomic():
                # since unique combination of source_field and slug exists, call save method
                super(KnowledgeBase, self).save(*args, **kwargs)

        except IntegrityError:
            """
            after catching the exception, we will generate another slug but this time we will
            suffix  it with a random string at the end of the slug to make it unique and try saving it again
            """
            self.slug = pl_custom_slugify(source_field=self.title, suffix=True)
            super(KnowledgeBase, self).save(*args, **kwargs)

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ['-modified_at', '-created_at']
        unique_together = ('title', 'slug')  # checks whether the combination of two fields is unique


class RandomData(RowInformation):
    """
    This class refers to all the random resources.
    It consists of attributes like title, description, slug, link_url,
    data_type and paid
    """
    title = models.CharField(max_length=100, null=False, blank=False)

    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True)
    link_url = models.URLField(null=False, blank=False, unique=True)

    # indicates the type of data, video, blog, tutorial, course or others
    data_type = models.CharField(max_length=2, choices=DATA_TYPES)

    # indicates whether the resource is paid or not
    paid = models.BooleanField(default=False)

    def save(self, *args, **kwargs):

        self.title = self.title.title() if self.title else self.title

        if not self.slug:
            self.slug = pl_custom_slugify(source_field=self.title, suffix=False)

        try:
            """
            While saving, it we have a duplicate combination of name and slug
            Since we have added an IntegrityError check, we will have an exception raised
            """
            #This will prevent the purposefully-thrown exception from breaking the entire unittest's transaction.
            with transaction.atomic():
                # since unique combination of source_field and slug exists, call save method
                super(RandomData, self).save(*args, **kwargs)

        except IntegrityError:
            """
            after catching the exception, we will generate another slug but this time we will
            suffix  it with a random string at the end of the slug to make it unique and try saving it again
            """
            self.slug = pl_custom_slugify(source_field=self.title, suffix=True)
            super(RandomData, self).save(*args, **kwargs)

    def __str__(self):
        return '{name}-{slug}'.format(name=self.title, slug=self.slug)

    class Meta:
        ordering = ['-modified_at', '-created_at']
        # checks whether the combination of two fields is unique
        unique_together = ('title', 'slug')

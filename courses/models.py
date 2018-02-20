from django.db import models
from courses.utils.constants import skill_levels, external_types, language_for, domain_for
from django.template.defaultfilters import slugify
from django.db import IntegrityError
from django.utils.crypto import get_random_string
# Create your models here.

"""
Non Critical: Please read a Pep8 guide or use an IDE such as PyCharm
"""


# move this to the utils - create a models utils
def custom_slugify(source_field, suffix=False):
    """
    Using django util methods create a slug.
    Append a random string at the end of the slug if necessary for making it unique
    """
    new_slug = slugify(source_field)  #slugify the source_field passed to the function

    if suffix:
        random_str = get_random_string(length=10)  #get a random string of length 10
        new_slug = "{0}-{1}".format(new_slug, random_str)  #the new_slug and random_str is concatenated

    return new_slug


class Language(models.Model):
    """
    It refers to the various languages in technical skills and soft skills context.
    This class consists of language attributes such as
    language_name, slug and languages_for
    """
    language_name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    # used to indicate whether the language is for technical skills or soft skills
    languages_for = models.CharField(max_length=2, choices=language_for)

    def save(self, *args, **kwargs):
        if not self.slug:
            # if slug doesn't exist pass the source_field and suffix=False to custom_slugify function
            self.slug = custom_slugify(source_field=self.language_name, suffix=False)

        try:
            """
            While saving, it we have a duplicate combination of name and slug
            Since we have added an IntegrityError check, we will have an exception raised
            """
            super(Language, self).save(*args, **kwargs)  #since unique combination of source_field and slug exists, call save method

        except IntegrityError:
            """
            after catching the exception, we will generate another slug but this time we will
            suffix  it with a random string at the end of the slug to make it unique and try saving it again
            """
            self.slug = custom_slugify(source_field=self.language_name, suffix=True)  #since unique combination of source_field and slug doesn't exist, pass suffix=True to add random_str to make it unique
            super(Language, self).save(*args, **kwargs)

    def __str__(self):
        return '{name}-{slug}'.format(name=self.language_name, slug=self.slug)

    class Meta:
        unique_together = ('language_name', 'slug')  #checks whether the combination of two fields is unique


class Domain(models.Model):
    """
    It refers to the various domains in the technical skills and soft skills context.
    This class consists of domain attributes such as
    domain_name, slug and domains_for
    """
    domain_name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    domains_for = models.CharField(max_length=2, choices=domain_for)  #used to indicate whether the domain is for technical skills or soft skills

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(source_field=self.domain_name, suffix=False)

        try:
            """
            While saving, it we have a duplicate combination of name and slug
            Since we have added an IntegrityError check, we will have an exception raised
            """
            super(Domain, self).save(*args, **kwargs)  #since unique combination of source_field and slug exists, call save method

        except IntegrityError:
            """
            after catching the exception, we will generate another slug but this time we will
            suffix  it with a random string at the end of the slug to make it unique and try saving it again
            """
            self.slug = custom_slugify(source_field=self.domain_name, suffix=True)  #since unique combination of source_field and slug doesn't exist, pass suffix=True to add random_str to make it unique
            super(Domain, self).save(*args, **kwargs)

    def __str__(self):
        return '{name}-{slug}'.format(name=self.domain_name, slug=self.slug)

    class Meta:
        unique_together = ('domain_name', 'slug')  #checks whether the combination of two fields is unique


# think about moving this to model utils
class RowInformation(models.Model):
    """
    This class is used to maintain meta information such as is_active, created_at, modified_at
    This can  be inherited in other classes to avoid making repeated attributes
    """
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  #used as a base class for other models


class KnowledgeBase(RowInformation):
    """
    This class is used to maintain attributes which are common to both the
    Video class and ExternalLink class. It inherits from RowInformation class
    """
    title = models.CharField(max_length=100, null=False, blank=False)  #title of the resource
    description = models.TextField(null=False, blank=True)    #if no description, store empty string
    slug = models.SlugField(unique=True)
    skill_level = models.CharField(max_length=2, choices=skill_levels)  #skill level required to understand the resource
    languages = models.ManyToManyField(Language, related_name='%(class)s_languages')  #languages associated with the resource
    domains = models.ManyToManyField(Domain, related_name='%(class)s_domains')  #domains associated with the resource

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(source_field=self.title, suffix=False)

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
            self.slug = custom_slugify(source_field=self.title, suffix=True)
            super(KnowledgeBase, self).save(*args, **kwargs)

    def __str__(self):
        return self.slug

    def multi_language(self):
        """
        check whether the resource has more than one languages associated
        with it, if yes return True
        """
        if self.languages.count() > 1:
            return True
        else:
            return False

    class Meta:
        abstract = True  #used as a base class for other models
        ordering = ['-modified_at','-created_at']
        unique_together = ('title', 'slug')  #checks whether the combination of two fields is unique

    multi_language.short_description = "multiple-languages"  #description to show on the admin panel
    multiple_languages = property(multi_language)   #multiple_languages is a property on KnowledgeBase
    multi_language.admin_order_field = '-modified_at'  #multi_language is ordered by reverse modified_at at the admin panel

    """
    Why not this convention?
    
    @property
    def multi_language(self):
        \"""
        check whether the resource has more than one languages associated
        with it, if yes return True
        \"""
        if self.languages.count() > 1:
            return True
        else:
            return False
    
    """


class Video(KnowledgeBase):
    """
    This is a class for resources which are either video or playlists. It inherits
    from the KnowledgeBase
    """
    video_url = models.URLField(null=False, blank=False, unique=True)  #url of the video resource


class ExternalLink(KnowledgeBase):
    """
    This is a class for resources which are external links, it can be a blog
    or a tutorial or a course. It inherits from the KnowledgeBase
    """
    link_url = models.URLField(null=False, blank=False, unique=True)  #url for ExternalLink resource
    external_type = models.CharField(max_length=2, choices=external_types)  #indicates whether the resource is a blog or a tutorial or course
    paid = models.BooleanField(default=False) #indicates whether the resource is paid or not

    class Meta:
        ordering = ['external_type']

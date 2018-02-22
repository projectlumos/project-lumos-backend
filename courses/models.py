from django.db import models
from courses.utils.constants import skill_levels, external_types, language_for, domain_for
from django.db import IntegrityError
from courses.utils import modelsutils
from courses.utils.modelsutils import RowInformation
# Create your models here.

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

    #used to indicate whether the language is for technical skills or soft skills
    languages_for = models.CharField(max_length=2, choices=language_for)

    def save(self, *args, **kwargs):
        if not self.slug:
            #if slug doesn't exist pass the source_field and suffix=False to custom_slugify function
            self.slug = modelsutils.custom_slugify(source_field=self.language_name, suffix=False)

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
            #since unique combination of source_field and slug doesn't exist, pass suffix=True to add random_str to make it unique
            self.slug = modelsutils.custom_slugify(source_field=self.language_name, suffix=True)
            super(Language, self).save(*args, **kwargs)

    def __str__(self):
        return '{name}-{slug}'.format(name=self.language_name, slug=self.slug)

    class Meta:
        #checks whether the combination of two fields is unique
        unique_together = ('language_name', 'slug')

class Domain(models.Model):
    """
    It refers to the various domains in the technical skills and soft skills context.
    This class consists of domain attributes such as
    domain_name, slug and domains_for
    """
    domain_name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    #used to indicate whether the domain is for technical skills or soft skills
    domains_for = models.CharField(max_length=2, choices=domain_for)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = modelsutils.custom_slugify(source_field=self.domain_name, suffix=False)

        try:
            """
            While saving, it we have a duplicate combination of name and slug
            Since we have added an IntegrityError check, we will have an exception raised
            """
            #since unique combination of source_field and slug exists, call save method
            super(Domain, self).save(*args, **kwargs)

        except IntegrityError:
            """
            after catching the exception, we will generate another slug but this time we will
            suffix  it with a random string at the end of the slug to make it unique and try saving it again
            """
            #since unique combination of source_field and slug doesn't exist, pass suffix=True to add random_str to make it unique
            self.slug = modelsutils.custom_slugify(source_field=self.domain_name, suffix=True)
            super(Domain, self).save(*args, **kwargs)

    def __str__(self):
        return '{name}-{slug}'.format(name=self.domain_name, slug=self.slug)

    class Meta:
        unique_together = ('domain_name', 'slug')  #checks whether the combination of two fields is unique


class KnowledgeBase(RowInformation):
    """
    This class is used to maintain attributes which are common to both the
    Video class and ExternalLink class. It inherits from RowInformation class
    """
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=True)    #if no description, store empty string
    slug = models.SlugField(unique=True)
    skill_level = models.CharField(max_length=2, choices=skill_levels)  # skill level required to understand the resource
    languages = models.ManyToManyField(Language, related_name='%(class)s_languages')  # languages associated with the resource
    domains = models.ManyToManyField(Domain, related_name='%(class)s_domains')  # domains associated with the resource

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
    #indicates whether the resource is a blog or a tutorial or course
    external_type = models.CharField(max_length=2, choices=external_types)
    paid = models.BooleanField(default=False) #indicates whether the resource is paid or not

    class Meta:
        ordering = ['external_type']

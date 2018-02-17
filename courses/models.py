from django.db import models
from courses.utils.constants import skill_levels, external_types, language_for, domain_for
from django.template.defaultfilters import slugify
from django.db import IntegrityError
from django.utils.crypto import get_random_string
# Create your models here.

def custom_slugify(source_field, suffix=False):
    new_slug = slugify(source_field)

    if suffix:
        random_str = get_random_string(length=10)
        new_slug = "{0}-{1}".format(new_slug, random_str)

    return new_slug

class Language(models.Model):
    language_name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    languages_for = models.CharField(max_length=2, choices=language_for)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(source_field=self.language_name, suffix=False)

        try:
            super(Language, self).save(*args, **kwargs)

        except IntegrityError:
            self.slug = custom_slugify(source_field=self.language_name, suffix=True)
            super(Language, self).save(*args, **kwargs)

    def __str__(self):
        return '{name}-{slug}'.format(name=self.language_name, slug=self.slug)

    class Meta:
        unique_together = ('language_name', 'slug')

class Domain(models.Model):
    domain_name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    domains_for = models.CharField(max_length=2, choices=domain_for)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(source_field=self.domain_name, suffix=False)

        try:
            super(Domain, self).save(*args, **kwargs)

        except IntegrityError:
            self.slug = custom_slugify(source_field=self.domain_name, suffix=True)
            super(Domain, self).save(*args, **kwargs)

    def __str__(self):
        return '{name}-{slug}'.format(name=self.domain_name, slug=self.slug)

    class Meta:
        unique_together = ('domain_name', 'slug')

class RowInformation(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class KnowledgeBase(RowInformation):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=True)    #if no description, store empty string
    slug = models.SlugField(unique=True)
    skill_level = models.CharField(max_length=2, choices=skill_levels)
    languages = models.ManyToManyField(Language, related_name='%(class)s_languages')
    domains = models.ManyToManyField(Domain, related_name='%(class)s_domains')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(source_field=self.title, suffix=False)

        try:
            super(KnowledgeBase, self).save(*args, **kwargs)

        except IntegrityError:
            self.slug = custom_slugify(source_field=self.title, suffix=True)
            super(KnowledgeBase, self).save(*args, **kwargs)

    def __str__(self):
        return self.slug

    def multi_language(self):
        if self.languages.count() > 1:
            return True
        else:
            return False
    class Meta:
        abstract = True
        ordering = ['-modified_at','-created_at']
        unique_together = ('title', 'slug')

    multi_language.short_description = "multiple-languages"
    multiple_languages = property(multi_language)
    multi_language.admin_order_field = '-modified_at'


class Video(KnowledgeBase):
    video_url = models.URLField(null=False, blank=False, unique=True)  #since video_id is a string

class ExternalLink(KnowledgeBase):
    link_url = models.URLField(null=False, blank=False, unique=True)
    external_type = models.CharField(max_length=2, choices=external_types)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['external_type']

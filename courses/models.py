from django.db import models
from utils.constants import SKILL_BEGINNER, SKILL_INTERMEDIATE, SKILL_ADVANCED, EXTERNAL_LINK_BLOG, EXTERNAL_LINK_TUTORIAL, EXTERNAL_LINK_COURSE
from django.utils.text import slugify
# Create your models here.

class Language(models.Model):
    language_name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)

    def _get_unique_slug(self):
        slug = slugify(self.language_name)
        unique_slug = slug
        num = 1
        while Language.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super(Language, self).save(*args, **kwargs)

    def __str__(self):
        return '{name}-{slug}'.format(name=self.language_name, slug=self.slug)


class Domain(models.Model):
    domain_name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)

    def _get_unique_slug(self):
        slug = slugify(self.domain_name)
        unique_slug = slug
        num = 1
        while Domain.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super(Domain, self).save(*args, **kwargs)

    def __str__(self):
        return '{name}-{slug}'.format(name=self.domain_name, slug=self.slug)

class RowInformation(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class KnowledgeBase(RowInformation):
    skill_levels = (
        (SKILL_BEGINNER, 'BEGINNER'),
        (SKILL_INTERMEDIATE, 'INTERMEDIATE'),
        (SKILL_ADVANCED, 'ADVANCED')
    )

    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=True)    #if no description, store empty string
    slug = models.SlugField(unique=True)
    languages = models.ManyToManyField(Language, related_name='knowledgebase_lang')
    domains = models.ManyToManyField(Domain, related_name='knowledgebase_dom')
    skill_level = models.CharField(max_length=2, choices=skill_levels)

    class Meta:
        abstract = True
        ordering = ['-modified_at','-created_at']

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while KnowledgeBase.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super(KnowledgeBase, self).save(*args, **kwargs)

    def __str__(self):
        return self.slug

    def multi_language(self):
        if self.languages.count() > 1:
            return True
        else:
            return False

    multi_language.short_description = "resource has multiple languages or not"
    multiple_languages = property(multi_language)


class Video(KnowledgeBase):
    video_id = models.URLField(null=False, blank=False, unique=True)  #since video_id is a string


class ExternalLink(KnowledgeBase):
    external_types = (     #indicate which type of external link
        (EXTERNAL_LINK_BLOG, 'BLOG'),
        (EXTERNAL_LINK_TUTORIAL, 'TUTORIAL'),
        (EXTERNAL_LINK_COURSE, 'COURSE')
    )

    link_url = models.URLField(null=False, blank=False, unique=True)
    external_type = models.CharField(max_length=2, choices=external_types)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['external_type']

from django.db import models
from utils.constants import SKILL_BEGINNER, SKILL_INTERMEDIATE, SKILL_ADVANCED, BLOGS, TUTORIALS, COURSES
from utils.utils import get_unique_slug
# Create your models here.

class Language(models.Model):
    language_name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'language_name', 'slug')
        super.save()

    def __str__(self):
        return '{name}-{slug}'.format(name=self.language_name, slug=self.slug)


class Domain(models.Model):
    domain_name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'domain_name', 'slug')
        super.save()

    def __str__(self):
        return '{name}-{slug}'.format(name=self.domain_name, slug=self.slug)

class KnowledgeBase(models.Model):
    skill_levels = (
        (SKILL_BEGINNER, 'BEGINNER'),
        (SKILL_INTERMEDIATE, 'INTERMEDIATE'),
        (SKILL_ADVANCED, 'ADVANCED')
    )

    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=True)    #if no description, store empty string
    slug = models.SlugField(unique=True)
    lang = models.ManyToManyField(Language, related_name='knowledgebase_lang')
    dom = models.ManyToManyField(Domain, related_name='knowledgebase_dom')
    _multi_language = models.BooleanField(db_column="multi_language")
    skill_level = models.CharField(max_length=2, choices=skill_levels)
    is_active = models.BooleanField(default=False)   #indicate whether the resource is active or not
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-modified_at','-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super.save()

    def __str__(self):
        return self.slug

    @property
    def multi_language(self):
        if self.lang.count() > 1:
            return True
        else:
            return False


class Video(KnowledgeBase):
    video_id = models.URLField(null=False, blank=False, unique=True)  #since video_id is a string


class ExternalLink(KnowledgeBase):
    external_types = (     #indicate which type of external link
        (BLOGS, 'BLOGS'),
        (TUTORIALS, 'TUTORIALS'),
        (COURSES, 'COURSES')
    )

    link_url = models.URLField(null=False, blank=False, unique=True)
    external_type = models.CharField(max_length=2, choices=external_types)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['external_type']

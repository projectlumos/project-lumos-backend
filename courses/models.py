from django.db import models

# Create your models here.

class Languages(models.Model):
    language_name = models.CharField(max_length=20)

    def __str__(self):
        return self.language_name


class Domains(models.Model):
    domain_name = models.CharField(max_length=20)

    def __str__(self):
        return self.domain_name

class KnowledgeBase(models.Model):
    SKILL_BEGINNER = 'beg'
    SKILL_INTERMEDIATE = 'int'
    SKILL_ADVANCED = 'adv'

    skill_levels = (
        (SKILL_BEGINNER, 'BEGINNER'),
        (SKILL_INTERMEDIATE, 'INTERMEDIATE'),
        (SKILL_ADVANCED, 'ADVANCED')
    )

    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=True)    #if no description, store empty string
    language = models.ManyToManyField(Languages)
    domain = models.ManyToManyField(Domains)
    multi_language = models.BooleanField(default=False)
    skill_level = models.CharField(max_length=3, choices=skill_levels)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Video(KnowledgeBase):
    video_id = models.CharField(max_length=100, unique=True)  #since video_id is a string

class Playlist(KnowledgeBase):
    playlist_id = models.CharField(max_length=100, unique=True) #since playlist_id is a string

class Course_link(KnowledgeBase):
    link_url = models.URLField(null=False, blank=False, unique=True)
    paid = models.BooleanField(default=False)

from django.db import models
from django.contrib.auth.models import User
from courses.utils.modelsutils import RowInformation
from ratings.utils.constants import RATING
from .managers import KnowledgeBaseRatingManager, SoftSkillsDataRatingManager, RandomDataRatingManager
import courses
# Create your models here.


class Rating(RowInformation):
    """
    This is a base class for rating models
    """
    # optional user foreignkey for anonymous users
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    attribute_1 = models.PositiveSmallIntegerField(default=0, choices=RATING)
    attribute_2 = models.PositiveSmallIntegerField(default=0, choices=RATING)
    attribute_3 = models.PositiveSmallIntegerField(default=0, choices=RATING)
    attribute_4 = models.PositiveSmallIntegerField(default=0, choices=RATING)

    class Meta:
        abstract = True


class KnowledgeBaseRating(Rating):
    """
    This class handles the ratings for KnowledgeBase resources
    """
    resource = models.ForeignKey('courses.KnowledgeBase', on_delete=models.CASCADE)

    objects = KnowledgeBaseRatingManager()


class SoftSkillsDataRating(Rating):
    """
    This class handles the ratings for SoftSkillsData resources
    """
    resource = models.ForeignKey('courses.SoftSkillsData', on_delete=models.CASCADE)

    objects = SoftSkillsDataRatingManager()


class RandomDataRating(Rating):
    """
    This class handles the ratings for RandomData resources
    """
    resource = models.ForeignKey('courses.RandomData', on_delete=models.CASCADE)

    objects = RandomDataRatingManager()

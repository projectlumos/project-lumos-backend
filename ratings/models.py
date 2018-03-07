from django.db import models
from courses.models import KnowledgeBase, SoftSkillsData, RandomData
from django.contrib.auth.models import User
from courses.utils.modelsutils import RowInformation
from ratings.utils.constants import RATING
# Create your models here.


class KnowledgeBaseRating(RowInformation):
    """
    This class handles the ratings for KnowledgeBase resources
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(KnowledgeBase, on_delete=models.CASCADE)
    attribute_1 = models.PositiveSmallIntegerField(default=0, choices=RATING)
    attribute_2 = models.PositiveSmallIntegerField(default=0, choices=RATING)
    attribute_3 = models.PositiveSmallIntegerField(default=0, choices=RATING)
    attribute_4 = models.PositiveSmallIntegerField(default=0, choices=RATING)

    class Meta:

        # user and resource ids together cannot be duplicated
        unique_together = ('user', 'resource')


class SoftSkillsDataRating(RowInformation):
    """
    This class handles the ratings for SoftSkillsData resources
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(SoftSkillsData, on_delete=models.CASCADE)
    attribute_1 = models.PositiveSmallIntegerField(default=0, choices=RATING)
    attribute_2 = models.PositiveSmallIntegerField(default=0, choices=RATING)
    attribute_3 = models.PositiveSmallIntegerField(default=0, choices=RATING)
    attribute_4 = models.PositiveSmallIntegerField(default=0, choices=RATING)

    class Meta:
        unique_together = ('user', 'resource')


class RandomDataRating(RowInformation):
    """
    This class handles the ratings for RandomData resources
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(RandomData, on_delete=models.CASCADE)
    attribute_1 = models.PositiveSmallIntegerField(default=0, choices=RATING)
    attribute_2 = models.PositiveSmallIntegerField(default=0, choices=RATING)
    attribute_3 = models.PositiveSmallIntegerField(default=0, choices=RATING)
    attribute_4 = models.PositiveSmallIntegerField(default=0, choices=RATING)

    class Meta:
        unique_together = ('user', 'resource')

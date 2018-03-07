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

    @property
    def get_avg_attribute1(self):
        """
        it gets all the objects from the current resource and grabs the values of attribute_1
        in a list, calculates the average rating for it and returns it
        """

        # gets a list of all the ratings for attribute_1 of the current resource by id
        qs = KnowledgeBaseRating.objects.filter(resource=self.resource).values_list('attribute_1', flat=True).order_by('id')

        # calculates the average of the qs list
        average = sum(qs)/float(len(qs))

        # rounds off the average to the closest 0.5
        result = round(average * 2) / 2.0
        return result

    @property
    def get_avg_attribute2(self):
        """
        it gets all the objects from the current resource and grabs the values of attribute_2
        in a list, calculates the average rating for it and returns it
        """
        qs = KnowledgeBaseRating.objects.filter(resource=self.resource).values_list('attribute_2', flat=True).order_by('id')
        average = sum(qs)/float(len(qs))
        result = round(average * 2) / 2.0
        return result

    @property
    def get_avg_attribute3(self):
        """
        it gets all the objects from the current resource and grabs the values of attribute_3
        in a list, calculates the average rating for it and returns it
        """
        qs = KnowledgeBaseRating.objects.filter(resource=self.resource).values_list('attribute_3', flat=True).order_by('id')
        average = sum(qs)/float(len(qs))
        result = round(average * 2) / 2.0
        return result

    @property
    def get_avg_attribute4(self):
        """
        it gets all the objects from the current resource and grabs the values of attribute_4
        in a list, calculates the average rating for it and returns it
        """
        qs = KnowledgeBaseRating.objects.filter(resource=self.resource).values_list('attribute_4', flat=True).order_by('id')
        average = sum(qs)/float(len(qs))
        result = round(average * 2) / 2.0
        return result

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

    @property
    def get_avg_attribute1(self):
        """
        it gets all the objects from the current resource and grabs the values of attribute_1
        in a list, calculates the average rating for it and returns it
        """
        qs = SoftSkillsDataRating.objects.filter(resource=self.resource).values_list('attribute_1', flat=True).order_by('id')
        average = sum(qs)/float(len(qs))
        result = round(average * 2) / 2.0
        return result

    @property
    def get_avg_attribute2(self):
        """
        it gets all the objects from the current resource and grabs the values of attribute_2
        in a list, calculates the average rating for it and returns it
        """
        qs = SoftSkillsDataRating.objects.filter(resource=self.resource).values_list('attribute_2', flat=True).order_by('id')
        average = sum(qs)/float(len(qs))
        result = round(average * 2) / 2.0
        return result

    @property
    def get_avg_attribute3(self):
        """
        it gets all the objects from the current resource and grabs the values of attribute_3
        in a list, calculates the average rating for it and returns it
        """
        qs = SoftSkillsDataRating.objects.filter(resource=self.resource).values_list('attribute_3', flat=True).order_by('id')
        average = sum(qs)/float(len(qs))
        result = round(average * 2) / 2.0
        return result

    @property
    def get_avg_attribute4(self):
        """
        it gets all the objects from the current resource and grabs the values of attribute_4
        in a list, calculates the average rating for it and returns it
        """
        qs = SoftSkillsDataRating.objects.filter(resource=self.resource).values_list('attribute_4', flat=True).order_by('id')
        average = sum(qs)/float(len(qs))
        result = round(average * 2) / 2.0
        return result

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

    @property
    def get_avg_attribute1(self):
        """
        it gets all the objects from the current resource and grabs the values of attribute_1
        in a list, calculates the average rating for it and returns it
        """
        qs = RandomDataRating.objects.filter(resource=self.resource).values_list('attribute_1', flat=True).order_by('id')
        average = sum(qs)/float(len(qs))
        result = round(average * 2) / 2.0
        return result

    @property
    def get_avg_attribute2(self):
        """
        it gets all the objects from the current resource and grabs the values of attribute_2
        in a list, calculates the average rating for it and returns it
        """
        qs = RandomDataRating.objects.filter(resource=self.resource).values_list('attribute_2', flat=True).order_by('id')
        average = sum(qs)/float(len(qs))
        result = round(average * 2) / 2.0
        return result

    @property
    def get_avg_attribute3(self):
        """
        it gets all the objects from the current resource and grabs the values of attribute_3
        in a list, calculates the average rating for it and returns it
        """
        qs = RandomDataRating.objects.filter(resource=self.resource).values_list('attribute_3', flat=True).order_by('id')
        average = sum(qs)/float(len(qs))
        result = round(average * 2) / 2.0
        return result

    @property
    def get_avg_attribute4(self):
        """
        it gets all the objects from the current resource and grabs the values of attribute_4
        in a list, calculates the average rating for it and returns it
        """
        qs = RandomDataRating.objects.filter(resource=self.resource).values_list('attribute_4', flat=True).order_by('id')
        average = sum(qs)/float(len(qs))
        result = round(average * 2) / 2.0
        return result

    class Meta:
        unique_together = ('user', 'resource')

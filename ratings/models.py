from django.db import models
from django.contrib.auth.models import User
from courses.utils.modelsutils import RowInformation
from ratings.utils.constants import RATING
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

    def calculate_ratings(self, attribute_list, resource):
        """
        it gets all the objects from the resource passed and grabs the values of attributes
        in a list, calculates the average rating for it and returns it
        """
        rating = []
        for item in attribute_list:
            try:
                qs = KnowledgeBaseRating.objects.filter(resource=resource).values_list(item, flat=True).order_by('id')
                # calculates the average of the qs list
                average = sum(qs)/float(len(qs))

                # rounds off the average to the closest 0.5
                result = round(average * 2) / 2.0

                # dictionary with key as item and value as the result
                result_dict = {item : result}

                # creates a list of dictionaries for the passed attributes
                rating.append(result_dict)

            except ZeroDivisionError:
                # handles when attribute is 0, returns empty list
                rating = []

        return rating


class SoftSkillsDataRating(Rating):
    """
    This class handles the ratings for SoftSkillsData resources
    """
    resource = models.ForeignKey('courses.SoftSkillsData', on_delete=models.CASCADE)

    def calculate_ratings(self, attribute_list, resource):
        """
        it gets all the objects from the resource passed and grabs the values of attributes
        in a list, calculates the average rating for it and returns it
        """
        rating = []
        for item in attribute_list:
            try:
                qs = SoftSkillsDataRating.objects.filter(resource=resource).values_list(item, flat=True).order_by('id')
                average = sum(qs)/float(len(qs))
                result = round(average * 2) / 2.0
                result_dict = {item : result}
                rating.append(result_dict)

            except ZeroDivisionError:
                rating = []

        return rating


class RandomDataRating(Rating):
    """
    This class handles the ratings for RandomData resources
    """
    resource = models.ForeignKey('courses.RandomData', on_delete=models.CASCADE)

    def calculate_ratings(self, attribute_list, resource):
        """
        it gets all the objects from the resource passed and grabs the values of attributes
        in a list, calculates the average rating for it and returns it
        """
        rating = []
        for item in attribute_list:
            try:
                qs = RandomDataRating.objects.filter(resource=resource).values_list(item, flat=True).order_by('id')
                average = sum(qs)/float(len(qs))
                result = round(average * 2) / 2.0
                result_dict = {item : result}
                rating.append(result_dict)

            except ZeroDivisionError:
                rating = []

        return rating

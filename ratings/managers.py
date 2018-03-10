from django.db import models


class KnowledgeBaseRatingQuerySet(models.QuerySet):
    def calculated_attribute_1(self):
        if self.exists():
            # flattening out only the attribute 1 and doing and avg of all the values
            average = sum(self.values_list('attribute_1', flat=True))/float(self.count())
            # rounding off to closest 0.5
            result = round(average * 2) / 2.0
            return result
        else:
            return 0

    def calculated_attribute_2(self):
        if self.exists():
            average = sum(self.values_list('attribute_2', flat=True))/float(self.count())
            result = round(average * 2) / 2.0
            return result
        else:
            return 0

    def calculated_attribute_3(self):
        if self.exists():
            average =  sum(self.values_list('attribute_3', flat=True))/float(self.count())
            result = round(average * 2) / 2.0
            return result
        else:
            return 0

    def calculated_attribute_4(self):
        if self.exists():
            average =  sum(self.values_list('attribute_4', flat=True))/float(self.count())
            result = round(average * 2) / 2.0
            return result
        else:
            return 0


class KnowledgeBaseRatingManager(models.Manager):
    """
    model manager for KnowledgeBaseRating
    """
    def get_queryset(self):
        return KnowledgeBaseRatingQuerySet(self.model, using=self._db)

    def calculated_attribute_1(self):
        return self.get_queryset().calculated_attribute_1()

    def calculated_attribute_2(self):
        return self.get_queryset().calculated_attribute_2()

    def calculated_attribute_3(self):
        return self.get_queryset().calculated_attribute_3()

    def calculated_attribute_4(self):
        return self.get_queryset().calculated_attribute_4()


class SoftSkillsDataRatingQuerySet(models.QuerySet):
    def calculated_attribute_1(self):
        if self.exists():
            average = sum(self.values_list('attribute_1', flat=True))/float(self.count())
            result = round(average * 2) / 2.0
            return result
        else:
            return 0

    def calculated_attribute_2(self):
        if self.exists():
            average = sum(self.values_list('attribute_2', flat=True))/float(self.count())
            result = round(average * 2) / 2.0
            return result
        else:
            return 0

    def calculated_attribute_3(self):
        if self.exists():
            average =  sum(self.values_list('attribute_3', flat=True))/float(self.count())
            result = round(average * 2) / 2.0
            return result
        else:
            return 0

    def calculated_attribute_4(self):
        if self.exists():
            average =  sum(self.values_list('attribute_4', flat=True))/float(self.count())
            result = round(average * 2) / 2.0
            return result
        else:
            return 0


class SoftSkillsDataRatingManager(models.Manager):
    """
    model manager for SoftSkillsDataRating
    """
    def get_queryset(self):
        return SoftSkillsDataRatingQuerySet(self.model, using=self._db)

    def calculated_attribute_1(self):
        return self.get_queryset().calculated_attribute_1()

    def calculated_attribute_2(self):
        return self.get_queryset().calculated_attribute_2()

    def calculated_attribute_3(self):
        return self.get_queryset().calculated_attribute_3()

    def calculated_attribute_4(self):
        return self.get_queryset().calculated_attribute_4()

class RandomDataRatingQuerySet(models.QuerySet):
    def calculated_attribute_1(self):
        if self.exists():
            average = sum(self.values_list('attribute_1', flat=True))/float(self.count())
            result = round(average * 2) / 2.0
            return result
        else:
            return 0

    def calculated_attribute_2(self):
        if self.exists():
            average = sum(self.values_list('attribute_2', flat=True))/float(self.count())
            result = round(average * 2) / 2.0
            return result
        else:
            return 0

    def calculated_attribute_3(self):
        if self.exists():
            average =  sum(self.values_list('attribute_3', flat=True))/float(self.count())
            result = round(average * 2) / 2.0
            return result
        else:
            return 0

    def calculated_attribute_4(self):
        if self.exists():
            average =  sum(self.values_list('attribute_4', flat=True))/float(self.count())
            result = round(average * 2) / 2.0
            return result
        else:
            return 0


class RandomDataRatingManager(models.Manager):
    """
    model manager for RandomDataRating
    """
    def get_queryset(self):
        return RandomDataRatingQuerySet(self.model, using=self._db)

    def calculated_attribute_1(self):
        return self.get_queryset().calculated_attribute_1()

    def calculated_attribute_2(self):
        return self.get_queryset().calculated_attribute_2()

    def calculated_attribute_3(self):
        return self.get_queryset().calculated_attribute_3()

    def calculated_attribute_4(self):
        return self.get_queryset().calculated_attribute_4()

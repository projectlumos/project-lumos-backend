from django.template.defaultfilters import slugify
from django.utils.crypto import get_random_string
from django.db import models


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


class RowInformation(models.Model):
    """
    This class is used to maintain meta information such as is_active, created_at, modified_at
    This can  be inherited in other classes to avoid making repeated attributes
    """
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  #used as a base class for other models
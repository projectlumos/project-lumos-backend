from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class LumosUser(models.Model):
    """
    A Separate class to store additional information 
    about the user.

    """
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="lumos_user")
    is_verified = models.BooleanField(default=False)

    class Meta:
        db_table = 'lumos_user'

    def __str__(self):
        return '{username}'.format(username=self.id.username)

from django.db import models
from django.contrib.auth.models import User


from utilities.app_utils.crpyto_utils import lumos_encryption_service
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

    @property
    def lumos_token(self):
        """
        
        :return: 
        """
        encrypted_token = lumos_encryption_service(data=str(self.id.id))

        return encrypted_token
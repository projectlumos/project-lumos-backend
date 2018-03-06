from django.db import models
from django.contrib.auth.models import (
	 BaseUserManager, AbstractBaseUser
	)
# Create your models here.


class UserManager(BaseUserManager):
    """
    We Use Model Manager to create a centralised area for 
    queries regarding the models

    """
    def create_user(self, email, password=None,is_active=True, is_staff=False, is_admin=False):
        """
        Creates and saves a User with the given email and password.

        """
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
        	raise ValueError('Users must have an password')

        user = self.model(
               email=self.normalize_email(email),
        )

        user.set_password(password)
        user.active = is_active
        user.staff = is_staff
        user.admin = is_admin
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.

        """
        user = self.create_user(
               email,
               password=password,
               is_staff=True
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.

        """
        user = self.create_user(
               email,
               password=password,
               is_staff=True,
               is_admin=True
        )
        
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """
    custom Django user model extending from AbstractBaseUser class.

    By default, Django User uses username for authentication purpose
    but since we require User's Email for authentication,
    we will inherit from AbstractBaseUser class and change the defaults.

    """
	email = models.EmailField(max_length=255,unique=True)
	active = models.BooleanField(default=True)

    # A Admin User who is not a superuser
	staff = models.BooleanField(default=False)

    # A Superuser  
	admin = models.BooleanField(default=False)  

	objects = UserManager()

	USERNAME_FIELD = 'email'


	def get_full_name(self):
        # The user is identified by their email address
		return self.email


	def get_short_name(self):
        # The user is identified by their email address
		return self.email


	def __str__(self):
		return self.email


	def has_perm(self, perm, obj=None):
        """
        Does the user have a specific permission?

        """
		return True


	def has_module_perms(self, app_label): 
	    """
        Does the user have permissions to view the app `app_label`?

        """
	    return True


	@property
	def is_staff(self):
		"""
        Is the user a member of staff?

        """
		return self.staff

	@property
	def is_admin(self):
		"""
        Is the user a admin member?

        """
		return self.admin

	@property
	def is_active(self):
		"""
        Is the user active?

        """
		return self.active








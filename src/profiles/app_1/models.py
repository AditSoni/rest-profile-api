from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager


# Create your models here.


class UserProfileManager(BaseUserManager):
    """ Helps user work with custom django model"""

    def create_user(self,email,name,password=None):
        """ Creates a new user profile object """

        if not email:
            raise ValueError('Users must Have an email address')


        email=self.normalize_email(email)
        user = self.model(email=email,name=name)

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self , email ,name ,password):
        """Creates a Admin or a SUper User"""

        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser,PermissionsMixin):
    """ Represents  a "user profile" in our system.   """

    email = models.EmailField( max_length=255,unique=True)
    name =  models.CharField(max_length=255) 
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS=['name']

    def get_full_name(self):
        """ Gets The full name from the user """
        
        return self.name

    def get_short_name(self):
        """Gets the short name of the user"""

        return self.name

    def __str__(self):
        """Converts objects into string format"""

        return self.email

class ProfileFeedItem(models.Model):
    """ user profile status and feeds"""

    user_profile = models.ForeignKey('UserProfile',on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        """ Return model as a string"""

        return self.status_text
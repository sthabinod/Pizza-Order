from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Its time to create a new custom user model



class MyAccountManager(BaseUserManager):

    # for creating usermanager must override these method

    # required fields in parameter
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("The email is required")

        if not username:
            raise ValueError("The username is required")

        # if they have username and email
        user = self.model(
            email= self.normalize_email(email),#converts email to lower case
            username  =username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self,email,username,password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
           
        )
        user.set_password(password)
        user.save(using=self._db)

    def create_superuser(self,email,username,password=None):
        # if they have username and email
        user = self.create_user(
            email=self.normalize_email(email),  # converts email to lower case
            username=username,
            password=password
        )

        user.is_admin = True
        user.is_staff =True
        user.is_superuser = True
        user.save(using = self._db)
        return user

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60,unique=True)
    username = models.CharField(max_length=30,unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    # Add anything you liek add here

    # Now adding fields that are required for abstract base user
    date_joined = models.DateTimeField(verbose_name='date joined',auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login',auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Login field
    USERNAME_FIELD = 'username'

    #Required field
    REQUIRED_FIELDS = ['email']


    objects = MyAccountManager()

    def __str__(self):
        return self.email

    # required function
    def has_perm(self,perm,obj = None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True

# Now Creating custom user manager

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from PIL import Image #
# Create your models here.


class MyAccountManager(BaseUserManager):

    def create_user(self, username, first_name, last_name, password=None):

        if not username:
            raise ValueError("Users must have an username")

        user = self.model(username=username, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, password):

        user = self.create_user(
            username=username, password=password, first_name=first_name,
            last_name=last_name,
         )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(verbose_name='email', max_length=100)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=50)
    # extra field for staff users
    # Bellow are different user types
    is_admin = models.BooleanField(default=False)
    is_webmaster = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'  # This defines the parameter we want to login with together with password
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = MyAccountManager()  # this calls the built up account manager

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"
        Simplest possible answer: Yes, always"""
        return self.is_admin

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always"""
        return True

class Profile(models.Model):
    user = models.OneToOneField(Account, null =True, on_delete=models.CASCADE)
    image = models.ImageField(default='profile/no-picture.jpg', upload_to='profile/profile_pics')
    def __str__(self):
        return f'{self.user.username} profile'
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 150 or img.width > 150:
            output_size = (150, 150)
            img.thumbnail(output_size)
            img.save(self.image.path)



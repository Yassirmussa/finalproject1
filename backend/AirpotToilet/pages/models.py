from django.db import models
from django.contrib.auth.models import AbstractUser


from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager  # Import the custom manager

class User(AbstractUser):
    UserID = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)

    username = None  # Removed username field

    USERNAME_FIELD = 'email'  # Specify email for login
    REQUIRED_FIELDS = []  # No other required fields

    objects = CustomUserManager()  # Use the custom user manager

    class Meta:
        db_table = 'users'

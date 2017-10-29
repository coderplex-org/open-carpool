from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """
    We can discuss and create the fields that are essential for User apart from existing fields
     I can think of
        - phone number
        - driver / passenger
    """
    pass


class Vehicle(models.Model):
    """
    We can discuss the details that are to be stored for a vehicle.
     I can think of
        - number of extra seats
        - vehicle number
        - foreign key relation with user
        - color
        - brand
    """
    pass

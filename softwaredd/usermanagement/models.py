from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Employee(User):
    """class for employee"""
    perm_usermanagement = models.BooleanField(default=False)
    perm_layout = models.BooleanField(default=False)
    perm_database = models.BooleanField(default=False)
    perm_offer = models.BooleanField(default=False)
    perm_offer_file = models.BooleanField(default=False)



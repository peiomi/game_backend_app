from django.db import models
from django.contrib.auth.models import AbstractUser

class Player(AbstractUser):
    account_created = models.DateTimeField(auto_now_add=True)
    last_login_ip = models.GenericIPAddressField(null=True, blank=True, default='')
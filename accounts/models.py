from django.db import models
from django.contrib.auth.models import User, AbstractUser
from uuid import uuid4


class Account(AbstractUser):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    email = models.CharField(max_length=100, unique=True)

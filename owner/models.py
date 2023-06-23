from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser





class User(AbstractUser):
    @property
    def name(self):
        return f"{self.user.first_name} - {self.user.last_name}"
    
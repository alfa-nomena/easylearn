from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.text import slugify
from uuid import uuid1





class Owner(AbstractUser):
    public_id = models.SlugField(blank=True)
    def save(self,*args, **kwargs):
        if not self.public_id:
            self.public_id = slugify(uuid1())
        return super().save(*args, **kwargs)
    
    @property
    def name(self):
        return f"{self.user.first_name} {self.user.last_name}"
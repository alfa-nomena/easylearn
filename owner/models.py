from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from uuid import uuid1






class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    public_id = models.SlugField()

    def save(self,*args, **kwargs):
        if not self.public_id:
            self.public_id = slugify(uuid1())
        return super().save(*args, **kwargs)
    
    @property
    def name(self):
        return f"{self.user.first_name} {self.user.last_name}"
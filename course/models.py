from typing import Iterable, Optional
from uuid import uuid1, uuid4
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

    
class Course(models.Model):
    public_id=models.SlugField(blank=True)
    title=models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateField(auto_now=True)
    
    
    def save(self,*args, **kwargs):
        if not self.public_id:
            self.public_id = slugify(uuid1())
        return super().save(*args, **kwargs)
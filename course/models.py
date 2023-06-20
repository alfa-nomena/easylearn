from uuid import uuid1
from django.db import models
from django.utils.text import slugify
from owner.models import Owner
    



class Course(models.Model):
    public_id=models.SlugField(blank=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    content = models.TextField()
    date_published = models.DateField(auto_now=True)
    
    
    def save(self,*args, **kwargs):
        if not self.public_id:
            self.public_id = slugify(uuid1())
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.title
    
    def __repr__(self) -> str:
        return str(self)
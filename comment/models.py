from uuid import uuid1
from django.db import models
from course.models import Course
from owner.models import User
from django.utils.text import slugify




class Comment(models.Model):
    public_id = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_published = models.DateField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def save(self,*args, **kwargs):
        if not self.public_id:
            self.public_id = slugify(uuid1())
        return super().save(*args, **kwargs)